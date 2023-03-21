class StreetViewImageScraper:
    def __init__(self):
        pass

    def scrape_images(self, coordinates):
        """
        Scrape street view images for the given coordinates.

        This method should be implemented by subclasses to handle specific street view image scraping techniques.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def get_scraped_images(self, coordinates):
        """
        Get the scraped images.

        :return: A list of images corresponding to the input coordinates.
        """
        imgs = self.scrape_images(coordinates)
        return imgs

    def __call__(self, *args, **kwargs):
        """Run and return output"""
        return self.get_scraped_images(
            kwargs.get("coordinates")
        )

    def __str__(self):
        return f"Street View Image Scraper"
