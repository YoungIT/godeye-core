from hydra import compose, initialize
from omegaconf import open_dict
from src.core.common.components.CountryGrid import CountryGrid
from src.core.common.location.COUNTRY import Country
from src.core.core import main
import pyrootutils

base_path = pyrootutils.find_root(search_from=__file__, indicator=[".git", "setup.cfg"])

def test_tibhannover_pipeline():
    with initialize(version_base="1.1", config_path="../configs"):
        cfg = compose(config_name="pipeline-tibhannover.yaml", overrides=[f"+geo-estimation.tib_hparams={base_path}/tests/assets/tibhannover/hparams.yaml"])

        for img in [
            "assets/imgs/london.jpeg",
            "assets/imgs/paris.jpeg",
            "assets/imgs/rome.jpeg",
        ]:
            with open_dict(cfg):
                cfg.img = img
            output = main(cfg)
