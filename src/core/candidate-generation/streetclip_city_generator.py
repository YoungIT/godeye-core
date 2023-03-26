from typing import List
from loguru import logger

from .streetclip_country_generator import StreetClipCountryCandidateGenerator
from .models.streetclip import StreetClipGenerator
from src.core.common.components.CityGrid import CityGrid
from src.core.common.components.GridCell import GridCell
from src.core.common.components.Grid import Grid

class StreetClipCityCandidateGenerator(StreetClipCountryCandidateGenerator):
    def __init__(
        self, 
        map_grids : Grid, 
        num_candidates : int = 1,
        model_name: str = "geolocal/StreetCLIP",
        use_torch_compiled: bool = False
    ):
        super(StreetClipCityCandidateGenerator, self).__init__(map_grids, 
                                                               num_candidates, 
                                                               model_name, 
                                                               use_torch_compiled)
        # init candidate generator
    def generate_candidates(self, image, metadata) -> dict:
        result_grid_candidate = CityGrid(preload=False)
        
        # Get candidate grid
        # Get country with highest probability
        countries_name = [c.name for c in self.countries]
        country_idx = self.generator(image.copy(), countries_name, num_candidates=1)[0]
        country_cell = self.countries[country_idx]  
        logger.debug(f"Country: {country_cell.name}")

        # Get city candidate          
        city_cells = country_cell.childs
        cities_name = [c.name for c in city_cells]

        candidate_idxs = self.generator(image, cities_name, num_candidates=self.num_candidates)

        for idx in candidate_idxs:
            result_grid_candidate.add_class(
                GridCell(name=cities_name[idx])
            )
        
        # DEBUG
        logger.debug("City candidate: ")
        result_grid_candidate.get_cell_names()
        
        return {
            "image": image,
            "grid_candidates": result_grid_candidate,
            "metadata": metadata,
        }