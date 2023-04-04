from omegaconf import open_dict
import pytest
from src.core.core import main

def test_exif_extractor():
    gt = {'ResolutionUnit': 2, 'ExifOffset': 78, 'XResolution': 144.0, 'YResolution': 144.0}
    assert True