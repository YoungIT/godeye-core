from typing import List, Tuple
from argparse import ArgumentParser
from math import ceil
from pathlib import Path
import torch
import pytorch_lightning as pl
import pandas as pd
from loguru import logger
import torchvision
from src.core.lib.GeoEstimation.classification.train_base import MultiPartitioningClassifier
from src.core.lib.GeoEstimation.classification.dataset import FiveCropImageDataset
from PIL import Image

import numpy as np
from .base import GeolocationEstimator
from src.core.common.utils.geography import lat_long_to_alpha2
from src.core.common.components.CountryGrid import CountryGrid
from src.core.core import base_path

class TIBHannoverEstimator(GeolocationEstimator):
    def __init__(
        self, 
        tib_checkpoint=f"{base_path}/resources/tibhannover/models/epoch=014-val_loss=18.4833.ckpt", 
        tib_hparams=f"{base_path}/resources/tibhannover/models/hparams.yaml",
        use_country_grid_candidates=False,
        device="cpu"
    ):
        super(TIBHannoverEstimator, self).__init__()
        self.model = MultiPartitioningClassifier.load_from_checkpoint(
            checkpoint_path=tib_checkpoint,
            hparams_file=tib_hparams,
            map_location=None,
        )
        self.model.eval()
        self.use_country_grid_candidates = use_country_grid_candidates
        self.device = device
        
        self.tfm = torchvision.transforms.Compose(
            [
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize(
                    (0.485, 0.456, 0.406), (0.229, 0.224, 0.225)
                ),
            ]
        )

    def preprocess_image(self, img):
        if(isinstance(img, str)):
            image = Image.open(img).convert("RGB")
        else:
            image = img
        image = torchvision.transforms.Resize(256)(image)
        crops = torchvision.transforms.FiveCrop(224)(image)
        crops_transformed = []
        for crop in crops:
            crops_transformed.append(self.tfm(crop))
    
        return torch.stack(crops_transformed, dim=0)
    
    def filter_output(self, 
                      coords_output: List[Tuple[float, float]], 
                      grid_candidates: CountryGrid
                      ):
        """Filter list of coordinates based on grid candidate.
        Remove all coordinates that not belong to Country candidate

        Args:
            coords_output (List[float, float]): List of lat, lng coord
            grid_candidates (CountryGrid): Country grid candidate
        """
        # Note: select only one country for test only
        candidate_country = grid_candidates.get_cells()[0]

        filter_coords = []
        for coord in coords_output:
            alpha2 = lat_long_to_alpha2(coord)

            if(alpha2 == candidate_country.repr_cls.alpha_2):
                filter_coords.append(coord)

        return filter_coords                

    def estimate_geolocation(
        self, 
        image: Image, 
        grid_candidates: CountryGrid, 
        metadata: dict = {}
    ):
        image = self.preprocess_image(image)

        X = [image.unsqueeze(0), {"img_path": "test"}]
        img_paths, pred_classes, pred_latitudes, pred_longitudes = self.model.inference(X)

        # Output contains 3 items, corresponding to different resolution
        output = self.model(image)

        num_hierarchy = len(self.model.hierarchy.partitionings)

        coords = []
        for idx in range(num_hierarchy):
            partition = self.model.hierarchy.partitionings[idx]
            partition_output = output[idx]

            cls_preds = torch.argmax(partition_output, dim=1)
            for cls_id in cls_preds.tolist():
                lat, lng = partition.get_lat_lng(cls_id)
                coords.append((lat, lng))
        
        # ASK: Whether or not using only country candidate with the highest probability only?
        coords = self.filter_output(coords, grid_candidates)
        logger.debug(coords)

        return {
            "image": image, 
            "grid_candidates": grid_candidates,
            "coordinates": coords,
            # "countries": countries
        }