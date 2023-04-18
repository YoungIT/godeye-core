import os
import json 
import pyrootutils
import pycountry
from geopy.geocoders import Nominatim

base_path = pyrootutils.find_root(search_from=__file__, indicator=[".git", "setup.cfg"])

COUNTRY_CONVERTER = json.load(open(os.path.join(base_path, "assets/metadata/alpha2_latlng.json")))
CITY_CONVERTER = json.load(open(os.path.join(base_path, "assets/metadata/city2latlng.json")))

ALPHA2_TO_COUNTRY_NAME = {}
for country in pycountry.countries:
    ALPHA2_TO_COUNTRY_NAME[country.alpha_2] = country.name

# NOMINATIM_CONVERTER = Nominatim(domain='localhost:8080/nominatim', scheme='http')
NOMINATIM_CONVERTER = Nominatim(user_agent="my-app")