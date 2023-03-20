import random
from .base import CandidateGenerator

class RandomCandidateGenerator(CandidateGenerator):
    def __init__(self, map_grids, num_candidates):
        super(RandomCandidateGenerator, self).__init__(map_grids)
        self.num_candidates = num_candidates
        
    def get_filter_info(self, image):
        return [0, self.num_candidates]
    
    def generate_candidates(self, image, metadata):
        filter_info = self.get_filter_info(image)
        
        return {
            "image": image,
            "grid_candidates": random.sample(self.map_grids, k=2),
            "metadata": metadata,
            "filter_info": filter_info,
        }
        
    def __call__(self, *args, **kwargs):
        return self.generate_candidates(
            kwargs.get("image"), 
            kwargs.get("metadata")
        )

