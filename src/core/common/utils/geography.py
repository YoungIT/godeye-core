from typing import Tuple

import reverse_geocoder as rg
from geopy.geocoders import Nominatim
from src.core.common.location.COUNTRY import Country
from src.core.common.utils.converter import (CITY_CONVERTER,
                                        COUNTRY_CONVERTER,
                                        NOMINATIM_CONVERTER,
                                        ALPHA2_TO_COUNTRY_NAME)

def country_to_lat_long_geopy(country_name: str):
    location = NOMINATIM_CONVERTER.geocode(country_name)
    if location:
        lat = location.latitude
        lng = location.longitude
        return lat, lng
    else:
        return None
    
def lat_long_to_place_geopy(coord: Tuple[float, float]):
    """Convert (lat, lng) to a place (city, country)

    Args:
        coord (Tuple): (lat, lng)
    """
    place = NOMINATIM_CONVERTER.reverse(coord)
    return place

def lat_long_to_alpha2(coord: Tuple[float, float]) -> str:
    """Convert (lat, lng) to alpha_2 code represent country"""
    results = rg.search(coord) # default mode = 2
    
    alpha2 = None
    if(len(results) > 0):
        alpha2 = results[0]["cc"]

    return alpha2
        
def country_to_lat_long_json(alpha2_code: str):
    """Convert alpha2 code represent country to country coordinate"""
    if(alpha2_code in COUNTRY_CONVERTER):
        lat, lng = COUNTRY_CONVERTER[country_name]
        return lat, lng
    else:
        return None
    
def city_to_lat_long_json(city_name: str):
    if(city_name in CITY_CONVERTER):
        lat, lng = CITY_CONVERTER[city_name]
        return lat, lng
    else:
        return None
    
if __name__ == "__main__":
    location = NOMINATIM_CONVERTER.geocode('Hanoi')
    lat_lon = (location.latitude, location.longitude)
    print(lat_lon)

    # print(lat_long_to_place((21.0294498, 105.8544441)))
