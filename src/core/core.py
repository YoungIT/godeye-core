from typing import List, Optional, Tuple

import hydra
from loguru import logger
from omegaconf import DictConfig, OmegaConf

def init_pipeline(cfg: DictConfig):    
    logger.info(f"Instantiating candidate generation module <{cfg['metadata-extractor']._target_}>")
    metadata_extractor = hydra.utils.instantiate(cfg["metadata-extractor"])
    
    logger.info(f"Instantiating candidate generation module <{cfg['candidate-generation']._target_}>")
    candidate_generator = hydra.utils.instantiate(cfg["candidate-generation"])

    logger.info(f"Instantiating candidate generation module <{cfg['geo-estimation']._target_}>")
    geo_estimator = hydra.utils.instantiate(cfg["geo-estimation"])

    logger.info(f"Instantiating candidate generation module <{cfg['streetview-image-scraper']._target_}>")
    image_scraper = hydra.utils.instantiate(cfg["streetview-image-scraper"])

    logger.info(f"Instantiating candidate generation module <{cfg['location-ranking']._target_}>")
    loc_ranker = hydra.utils.instantiate(cfg["location-ranking"])
    
    pipeline = [
        metadata_extractor, 
        candidate_generator,
        geo_estimator, 
        image_scraper,
        loc_ranker
    ]
    
    return pipeline

@hydra.main(config_path="../../configs", config_name="run.yaml", version_base="1.1")
def main(cfg: DictConfig):
    logger.info(f"\nConfigs: \n {OmegaConf.to_yaml(cfg)}")
    pipeline = init_pipeline(cfg)
    output = {
        "image": cfg.img
    }
    for module in pipeline:
        output = module(**output)
        logger.info(f"{module}: {output}")
    return output

if __name__ == "__main__":
    main()