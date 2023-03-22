from .base import LocationRanker

class RandomLocationRanker(LocationRanker):
    def compute_scores(self, imgs, ref_img):
        scores = []
        for img in imgs:
            scores.append(10.)
        return scores