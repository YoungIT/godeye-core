import hydra
import pytest
from src.core.core import main
from omegaconf import open_dict

@hydra.main(config_path="../configs", config_name="test.yaml", version_base="1.1")
def test_pipeline(cfg):
    for img in [
        "./assets/london.jpg",
        "./assets/paris.jpg",
        "./assets/rome.jpg",
    ]:
        with open_dict(cfg):
            cfg.img = img
        output = main(cfg)
        
        print(output)
        
if __name__ == "__main__":
    test_pipeline()
