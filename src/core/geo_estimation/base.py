class GeolocationEstimator:
    def __init__(self):
        pass

    def estimate_geolocation(self, image, grid_candidates, metadata=None):
        """
        Estimate geolocation from the given image.

        This method should be implemented by subclasses to handle specific geolocation estimation techniques.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def get_coordinates(self, image, grid_candidates, metadata=None):
        """
        Get the estimated coordinates.

        :return: A list of coordinates representing the estimated geolocations.
        """
        grids = self.estimate_geolocation(image, grid_candidates, metadata)
        return grids

    def __call__(self, *args, **kwargs):
        return self.get_coordinates(kwargs.get("image").copy(), kwargs.get("grid_candidates"), metadata=kwargs.get("metadata"))

    def __str__(self):
        return f"Geolocation Estimator"