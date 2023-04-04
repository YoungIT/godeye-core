from .base import MetadataExtractor

class EmptyMetadataExtractor(MetadataExtractor):
    def extract_metadata(self, image):
        metadata = {}
        return metadata