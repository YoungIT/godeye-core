from .base import StreetViewImageScraper

class RandomImageScraper(StreetViewImageScraper):
    def scrape_images(self, **kwargs):
        return {
            "coordinates": kwargs.get("coordinates"),
            "image_candidates": [
                ["assets/imgs/london.jpeg", "assets/imgs/paris.jpeg", "assets/imgs/rome.jpeg"]
                for coord in kwargs.get("coordinates")
            ],
            "image": kwargs.get("image"),
            "countries": kwargs.get("countries")
        }