from .base import StreetViewImageScraper

"""
noop class
"""
class EmptyImageScraper(StreetViewImageScraper):
    def scrape_images(self, **kwargs):
        return {
            "coordinates": kwargs.get("coordinates"),
            "image_candidates": [
                []
                for coord in kwargs.get("coordinates")
            ],
            "image": kwargs.get("image").copy(),
            "countries": kwargs.get("countries")
        }