from typing import Dict

class CandidateGenerator:
    def __init__(self, map_grids):
        self.map_grids = map_grids
        
    def get_filter_info(self):
        """Get info to filter grid based on AI model"""
        raise NotImplementedError("Subclasses should implement this method.")

    def generate_candidates(self, image, metadata: Dict):
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
        """Run and return output"""
        raise NotImplementedError("Subclasses should implement this method.")

    def __str__(self):
        return f"Candidate Generator"