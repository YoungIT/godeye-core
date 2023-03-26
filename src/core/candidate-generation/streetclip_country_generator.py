from typing import List

from .base import CandidateGenerator
from .models.streetclip import StreetClipGenerator
from src.core.common.components.CountryGrid import CountryGrid
from src.core.common.components.GridCell import GridCell
from src.core.common.components.Grid import Grid
class StreetClipCountryCandidateGenerator(CandidateGenerator):
    def __init__(
        self, 
        map_grids : Grid, 
        num_candidates : int = 1,
        model_name: str = "geolocal/StreetCLIP",
        use_torch_compiled: bool = False
    ):
        super(StreetClipCountryCandidateGenerator, self).__init__(map_grids, num_candidates)
        # init candidate generator
        self.generator = StreetClipGenerator(model_name, use_torch_compiled)
        self.countries = self.map_grids.get_cells()

    def generate_candidates(self, image, metadata) -> dict:
        result_grid_candidate = CountryGrid(preload=False)
        
        # Get candidate grid
        countries_name = [c.name for c in self.countries]
        candidate_idxs = self.generator(image, countries_name, self.num_candidates)
        for idx in candidate_idxs:
            result_grid_candidate.add_class(
                GridCell(name=countries_name[idx])
            )
        
        # DEBUG
        result_grid_candidate.get_cell_names()
        
        return {
            "image": image,
            "grid_candidates": result_grid_candidate,
            "metadata": metadata,
        }
