from geopy.geocoders import Nominatim
from src.core.common.location.COUNTRY import Country
from src.core.common.utils.coord_converter import CITY_CONVERTER, COUNTRY_CONVERTER

def country_to_lat_long_geopy(country_name):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(country_name)
    if location:
        lat = location.latitude
        lng = location.longitude
        return lat, lng
    else:
        return None

def country_to_lat_long_json(country_name):
    if(country_name in COUNTRY_CONVERTER):
        lat, lng = COUNTRY_CONVERTER[country_name]
        return lat, lng
    else:
        return None
    
def city_to_lat_long_json(city_name):
    if(city_name in CITY_CONVERTER):
        lat, lng = CITY_CONVERTER[city_name]
        return lat, lng
    else:
        return None
    

