from hydra import compose, initialize
from omegaconf import open_dict
import pytest
from src.core.core import main

def test_pipeline():
    with initialize(version_base="1.1", config_path="../configs"):
        cfg = compose(config_name="pipeline-random.yaml", overrides=[])
        for img in [
            "assets/london.jpeg",
            "assets/paris.jpeg",
            "assets/rome.jpeg",
        ]:
            with open_dict(cfg):
                cfg.img = img
            output = main(cfg)
