from PIL import Image
from PIL.ExifTags import TAGS

def extract_exif(image_path):
    with Image.open(image_path) as img:
        exifdata = img.getexif()
        metadata = {}
        for tag_id, value in exifdata.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value
    return metadata