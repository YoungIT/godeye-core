from .base import MetadataExtractor

class EmptyMetadataExtractor(MetadataExtractor):
    def extract_metadata(self, image):
        metadata = {
            "image": image
        }
        return metadata
    
    def __call__(self, *args, **kwargs):
        return self.extract_metadata(kwargs.get("image"))