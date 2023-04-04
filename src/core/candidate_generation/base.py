import numpy as np
from typing import Dict
from src.core.common.components.Grid import Grid

class CandidateGenerator:
    def __init__(
        self, 
        map_grids : Grid, 
        num_candidates : int =1
    ):
        self.map_grids = map_grids
        self.num_candidates = num_candidates
        
    def get_filter_info(self):
        """Get info to filter grid based on AI model"""
        raise NotImplementedError("Subclasses should implement this method.")

    def generate_candidates(
        self, 
        image: np.array, 
        metadata: Dict
    ):
        """
        Generate candidates from the given image and metadata.

        This method should be implemented by subclasses to handle specific candidate generation techniques.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def get_candidates(self, image, metadata: Dict):
        """
        Get the generated candidates.

        :return: A list of grids representing the candidates.
        """
        candidate_grids, filter_info = self.generate_candidates(image, metadata)
        return candidate_grids, filter_info

    def __call__(self, *args, **kwargs):
        return self.generate_candidates(
            kwargs.get("image"), 
            kwargs.get("metadata")
        )

    def __str__(self):
        return f"Candidate Generator"