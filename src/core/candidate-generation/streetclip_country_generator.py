from typing import List

import torch
import numpy as np
from transformers import CLIPProcessor, CLIPModel

from .base import CandidateGenerator
from src.core.common.components.CountryGrid import CountryGrid
from src.core.common.components.GridCell import GridCell
from src.core.common.components.Grid import Grid
from src.core.common.location.COUNTRY import Country

class StreetClipCountryCandidateGenerator(CandidateGenerator):
    def __init__(
        self, 
        map_grids : Grid, 
        num_candidates : int = 1,
        model_name: str = "geolocal/StreetCLIP"
    ):
        super(StreetClipCountryCandidateGenerator, self).__init__(map_grids, num_candidates)
        # init candidate generator
        self.generator = StreetClipGenerator(model_name)
        self.countries = [grid_cell.name for grid_cell in self.map_grids.get_cells()]

    def generate_candidates(self, image, metadata) -> dict:
        result_grid_candidate = CountryGrid(preload=False)
        
        # Get candidate grid
        candidate_idxs = self.generator(image, self.countries, self.num_candidates)
        for idx in candidate_idxs:
            result_grid_candidate.add_class(
                GridCell(name=self.countries[idx])
            )
        
        # DEBUG
        result_grid_candidate.get_cell_names()
        
        return {
            "image": image,
            "grid_candidates": result_grid_candidate,
            "metadata": metadata,
        }

class StreetClipGenerator():
    def __init__(self, model_name):
        self.model = CLIPModel.from_pretrained(model_name)
        self.processor = CLIPProcessor.from_pretrained(model_name)

    def __call__(self, image, choices: List[str], num_candidates: int = 5):
        with torch.no_grad():
            inputs = self.processor(text=choices, images=image, return_tensors="pt", padding=True)
            # if(img_feature is None):
            #     img_feature = inputs["pixel_values"]
                
            outputs = self.model(**inputs)
            # decode output
            logits_per_image = outputs.logits_per_image # this is the image-text similarity score
            probs = logits_per_image.softmax(dim=1)[0].detach().cpu().numpy() # we can take the softmax to get the label probabilities
            candidate_idxs = np.argsort(probs)[-num_candidates:][::-1]
            
            return candidate_idxs
