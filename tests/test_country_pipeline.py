from hydra import compose, initialize
from omegaconf import open_dict
from src.core.common.components.CountryGrid import CountryGrid
from src.core.common.location.COUNTRY import Country
from src.core.core import main

def test_init_country_grid():
    country_grid = CountryGrid(preload=True)
    assert country_grid.num_classes == len(Country)
    for cell in country_grid.get_cells():
        assert cell.repr_cls in [c.value for c in Country]

def test_country_pipeline():
    with initialize(version_base="1.1", config_path="../configs"):
        cfg = compose(config_name="pipeline-country.yaml", overrides=[])
        for img in [
            "assets/imgs/london.jpeg",
            "assets/imgs/paris.jpeg",
            "assets/imgs/rome.jpeg",
        ]:
            with open_dict(cfg):
                cfg.img = img
            output = main(cfg)
