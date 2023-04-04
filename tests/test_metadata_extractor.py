from PIL import Image
from src.core.metadata_extractor.exif_extractor import extract_exif

def test_exif_extractor():
    exif_image_path = "assets/imgs/img_with_exif.png"
    with Image.open(exif_image_path).convert("RGB") as img:
        extracted_metadata = extract_exif(img)
        actual_metadata = {'ResolutionUnit': 2, 'ExifOffset': 78, 'XResolution': 144.0, 'YResolution': 144.0}
        assert extracted_metadata == actual_metadata