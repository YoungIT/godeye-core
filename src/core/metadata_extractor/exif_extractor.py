from PIL import Image
from PIL.ExifTags import TAGS

def get_image_metadata(image_path):
    with Image.open(image_path) as img:
        exifdata = img.getexif()
        metadata = {}
        for tag_id, value in exifdata.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value
    return metadata

if __name__ == '__main__':
    image_path = 'assets/imgs/img_with_exif.png' # Replace with your image path
    metadata = get_image_metadata(image_path)
    print(metadata)