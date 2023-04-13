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

if __name__ == "__main__":
    test_country_name()