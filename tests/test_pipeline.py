import hydra
import pytest
from src.core.core import main
from omegaconf import open_dict

def test_pipeline(cfg):
    for img in [
        "./assets/london.jpg",
        "./assets/paris.jpg",
        "./assets/rome.jpg",
    ]:
        with open_dict(cfg):
            cfg.img = img
        output = main(cfg)
