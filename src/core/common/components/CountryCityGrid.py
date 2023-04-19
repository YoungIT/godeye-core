from dataclasses import dataclass
from collections import defaultdict

from .Grid import Grid
from ..location.CITY import City
from ..location.COUNTRY import Country
from .GridCell import GridCell

class CountryCityGrid(Grid):
    @staticmethod
    def get_country_group():
        country_names = [item.name for item in Country]
        country_group = defaultdict(list)

        for city in City:
            elem_parts = city.name.split("_")
            city_name, country_name = "_".join(elem_parts[:-1]), elem_parts[-1]
            if country_name not in country_names:
                group_key = "Unknown"
            else:
                group_key = Country[country_name].value.name
            country_group[group_key].append(city.value)
        
        return country_group

    def load_cell_info(self):
        country_group = self.get_country_group()

        for country in Country:
            cities = country_group[country.value.name]
            self.add_class(
                GridCell(
                    name=country.value.name,
                    repr_cls=country.value,
                    childs=[GridCell(name=city) for city in cities]
                )
            )