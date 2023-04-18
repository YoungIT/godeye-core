from argparse import ArgumentParser
from math import ceil
from pathlib import Path
import torch
import pytorch_lightning as pl
import pandas as pd
import torchvision
from src.core.lib.GeoEstimation.classification.train_base import MultiPartitioningClassifier
from src.core.lib.GeoEstimation.classification.dataset import FiveCropImageDataset
from PIL import Image

import numpy as np
from .base import GeolocationEstimator
from src.core.common.utils.geography import country_to_lat_long_json
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

    def preprocess_image(self, img_path):
        image = Image.open(img_path).convert("RGB")
        image = torchvision.transforms.Resize(256)(image)
        crops = torchvision.transforms.FiveCrop(224)(image)
        crops_transformed = []
        for crop in crops:
            crops_transformed.append(self.tfm(crop))
    
        return torch.stack(crops_transformed, dim=0)

    def estimate_geolocation(
        self, 
        image: np.array, 
        grid_candidates: CountryGrid, 
        metadata: dict = {}
    ):
        # Change shape from h x w x c to c x h x w
        # image = np.swapaxes(image, 0, 2)
        # image = np.swapaxes(image, 1, 2)
        # image = torch.tensor(image).to(self.device).float()
        image = self.preprocess_image("/home/yitec/WORK/tung/godeye-core/assets/imgs/london.jpeg")

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

        countries = grid_candidates.get_cells()
        print("Country list", [c.name for c in countries])

        return {
            "image": image,
            "grid_candidates": grid_candidates,
            "coordinates": coords,
            # "countries": countries
        }