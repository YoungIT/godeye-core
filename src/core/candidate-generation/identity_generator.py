from .base import CandidateGenerator

class IdentityCandidateGenerator(CandidateGenerator):
    def generate_candidates(self, image, metadata):
        return {
            "image": image,
            "grid_candidates": self.map_grids,
            "metadata": metadata,
        }

