from .base import LocationRanker

class RandomLocationnRanker(LocationRanker):
    def compute_scores(self, imgs, ref_img):
        scores = []
        for img in imgs:
            scores.append(1.)
        return scores