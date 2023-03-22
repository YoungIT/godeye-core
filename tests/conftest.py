# """This file prepares config fixtures for other tests."""

# import pyrootutils
# import pytest
# from hydra import compose, initialize
# from hydra.core.global_hydra import GlobalHydra
# from omegaconf import DictConfig, open_dict

# @pytest.fixture(scope="package")
# def cfg_global() -> DictConfig:
#     with initialize(version_base="1.3", config_path="../configs"):
#         cfg = compose(config_name="run.yaml", return_hydra_config=True, overrides=[])

#         # set defaults for all tests
#         with open_dict(cfg):
#             cfg.logger = None

#     return cfg

# # this is called by each test which uses `cfg` arg
# # each test generates its own temporary logging path
# @pytest.fixture(scope="function")
# def cfg(cfg_global, tmp_path) -> DictConfig:
#     cfg = cfg_global.copy()

#     yield cfg

#     GlobalHydra.instance().clear()
