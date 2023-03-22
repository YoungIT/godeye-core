from .base import GeolocationEstimator

class RandomGeolocationEstimator(GeolocationEstimator):
    def estimate_geolocation(self, image, grid_candidates, metadata=None):
        return {
            "image": image,
            "coordinates": [
                [21, 105],
                [22, 104],
            ],
        }