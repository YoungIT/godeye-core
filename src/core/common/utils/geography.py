from typing import Tuple

from geopy.geocoders import Nominatim
from src.core.common.location.COUNTRY import Country
from src.core.common.utils.coord_converter import (CITY_CONVERTER,
                                                   COUNTRY_CONVERTER,
                                                   NOMINATIM_CONVERTER)

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

def country_to_lat_long_json(country_name: str):
    if(country_name in COUNTRY_CONVERTER):
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

    print(lat_long_to_place((21.0294498, 105.8544441)))
