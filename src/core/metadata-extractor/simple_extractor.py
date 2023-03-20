from .base import MetadataExtractor

class SimpleMetadataExtractor(MetadataExtractor):
    def extract_metadata(self, image):
        metadata = {}
        return metadata
    
    def __call__(self, *args, **kwargs):
        return self.extract_metadata(kwargs.get("image"))