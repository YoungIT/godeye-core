import numpy as np
from .base import GeolocationEstimator
from src.core.common.utils.geography import city_to_lat_long_json
from src.core.common.components.CityGrid import CityGrid

class CityToCoordEstimator(GeolocationEstimator):
    def estimate_geolocation(
        self, 
        image: np.array, 
        grid_candidates: CityGrid, 
        metadata: dict = {}
    ):
        cities = grid_candidates.get_cells()
        return {
            "image": image,
            "grid_candidates": grid_candidates,
            "coordinates": [
                city_to_lat_long_json(cell.name)
                for cell in cities
            ],
            "countries": cities
        }