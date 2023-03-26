from .Grid import Grid
from ..location.CITY import City
from .GridCell import GridCell

class CityGrid(Grid):
    def load_cell_info(self):
        for city in City:
            self.add_class(
                GridCell(
                    name=city.value,
                )
            )