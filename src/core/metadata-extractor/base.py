from typing import Dict

class MetadataExtractor:
    def __init__(self):
        pass

    def extract_metadata(self, image) -> Dict:
        """Extract metadata from the given image"""
        raise NotImplementedError("Subclasses should implement this method.")

    def get_metadata(self, image) -> Dict:
        """
        Get the extracted metadata.

        :return: A dictionary containing the extracted metadata.
        """
        metadata = self.extract_metadata(image)
        return metadata

    def __call__(self, *args, **kwargs):
        """Run and return output"""
        raise NotImplementedError("Subclasses should implement this method.")

    def __str__(self):
        return f"Metadata Extractor"