from dataclasses import dataclass
from .Grid import Grid
from ..location.COUNTRY import Country
from .GridCell import GridCell

class CountryGrid(Grid):
    def load_cell_info(self):
        for country in Country:
            self.add_class(
                GridCell(
                    name=country.value,
                )
            )