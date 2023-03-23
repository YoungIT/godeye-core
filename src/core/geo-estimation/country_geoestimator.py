import numpy as np
from .base import GeolocationEstimator
from src.core.common.utils.geography import country_to_lat_long
from src.core.common.components.CountryGrid import CountryGrid
from src.core.common.location.COUNTRY import Country

class CountryToCoordEstimator(GeolocationEstimator):
    def estimate_geolocation(
        self, 
        image: np.array, 
        grid_candidates: CountryGrid, 
        metadata: dict = {}
    ):
        countries = grid_candidates.get_cells()
        return {
            "image": image,
            "grid_candidates": grid_candidates,
            "coordinates": [
                country_to_lat_long(cell.name)
                for cell in countries
            ],
            "countries": countries
        }