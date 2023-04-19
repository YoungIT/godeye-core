import pycountry

from src.core.common.location.COUNTRY import Country

def test_country_name():
    pycountry_alpha2 = [country.alpha_2 for country in pycountry.countries]
    pycountry_countries = [country.name for country in pycountry.countries]
    print(pycountry_countries)

    mapper = {}
    for country in pycountry.countries:
        mapper[country.name] = country.alpha_2

    file = open("test.txt", "w")
    
    for country in Country:
        if(country.value not in pycountry_countries):
            print(country.value)
        else:
            text_formatted = f'{country.name}: CountryStruct = CountryStruct("{country.value}", "{mapper[country.value]}")'
            print(text_formatted)

            # file.write(f"{text_formatted}\n")
            
def get_alpha2_to_coord():
    import json
    
    with open("../assets/metadata/country2latlng.json", "r") as f:
        data = json.load(f)
        
    mapper = {}
    for country in pycountry.countries:
        mapper[country.name] = country.alpha_2
        
    
    alpha2_to_coord = {}
    for country_name, coord in data.items():
        if(country_name in mapper):
            alpha2_to_coord[mapper[country_name]] = coord
        else:
            print(country_name)
            
    with open("../assets/metadata/country2latlng_v2.json", "w") as f:
        json.dump(alpha2_to_coord, f)

if __name__ == "__main__":
    get_alpha2_to_coord()