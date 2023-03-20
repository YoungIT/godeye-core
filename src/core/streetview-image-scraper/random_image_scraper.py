from .base import StreetViewImageScraper

class RandomImageScraper(StreetViewImageScraper):
    def scrape_images(self, coordinates):
        return {
            "image_candidates": [
                {
                    "coord": coord,
                    "images": ["./assets/london.jpeg", "./assets/paris.jpeg", "./assets/rome.jpeg"]
                }
                for coord in coordinates
            ]
        }