from geopy.geocoders import Nominatim

def country_to_lat_long(country_name):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(country_name)
    if location:
        lat = location.latitude
        lng = location.longitude
        return lat, lng
    else:
        return None