from PIL.ExifTags import TAGS
from .base import MetadataExtractor

def extract_exif(img):
    exifdata = img.getexif()
    metadata = {}
    for tag_id, value in exifdata.items():
        tag = TAGS.get(tag_id, tag_id)
        metadata[tag] = value
    return metadata


class ExifMetadataExtractor(MetadataExtractor):
    def extract_metadata(self, image):
        metadata = extract_exif(image.copy())
        return metadata