import random
from .base import CandidateGenerator
from src.core.common.components.CandidateGenerationOutput import *
from src.core.common.components.CountryGrid import CountryGrid
from src.core.common.components.GridCell import GridCell
from src.core.common.location.COUNTRY import Country

class RandomCandidateGenerator(CandidateGenerator):
    def generate_candidates(self, image, metadata):
        result_grid_candidate = CountryGrid(preload=False)
        result_grid_candidate.add_class(
            GridCell(name=Country.UnitedStates.value)
        )
        result_grid_candidate.add_class(
            GridCell(name=Country.Canada.value)
        )

        return {
            "image": image,
            "grid_candidates": result_grid_candidate,
            "metadata": metadata
        }

        # return CandidateGenerationOutput(
        #     image=image,
        #     grid_candidates=result_grid_candidate,
        #     metadata=metadata
        # )