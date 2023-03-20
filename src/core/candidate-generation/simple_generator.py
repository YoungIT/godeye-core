import random
from .base import CandidateGenerator

class RandomCandidateGenerator(CandidateGenerator):
    def __init__(self, map_grids, num_candidates):
        super(RandomCandidateGenerator, self).__init__(map_grids)
        self.num_candidates = num_candidates
        
    def get_filter_info(self, image):
        return [0, 20]
    
    def generate_candidates(self, image, metadata):
        filter_info = self.get_filter_info(image)
        for _ in range(self.num_candidates):
            grid_idxs = random.randint(filter_info[0], filter_info[1])
            
        return self.map_grids[grid_idxs], filter_info
        