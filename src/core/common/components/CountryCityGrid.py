from dataclasses import dataclass
from collections import defaultdict

from .Grid import Grid
from ..location.CITY import City
from ..location.COUNTRY import Country
from .GridCell import GridCell

class CountryCityGrid(Grid):
    @staticmethod
    def get_country_group():
        country_group = defaultdict(list)

        # country_dict = dict(Country)
        for city in City:
            elem_parts = city.name.split("_")
            city_name, country_name = "_".join(elem_parts[:-1]), elem_parts[-1]
            country_group[Country[country_name].value].append(city.value)
        
        return country_group

    def load_cell_info(self):
        country_group = self.get_country_group()

        print(country_group.keys())

        for country in Country:
            cities = country_group[country.value]
            self.add_class(
                GridCell(
                    name=country.value,
                    childs=[GridCell(name=city) for city in cities]
                )
            )