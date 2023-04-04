class LocationRanker:
    def __init__(self):
        pass

    def compute_scores(self, imgs, ref_img):
        """
        Compute scores for the given images based on their similarity to the reference image.

        This method should be implemented by subclasses to handle specific location ranking techniques.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def get_scores(self, imgs, ref_img):
        """
        Get the computed scores.

        :return: A list of scores representing the similarity of each image to the reference image.
        """
        scores = self.compute_scores(imgs, ref_img)
        return scores

    def __call__(self, *args, **kwargs):
        """Run and return output"""
        scores = []
        coordinates = kwargs.get("coordinates")
        for idx, image_candidate in enumerate(kwargs.get("image_candidates")):
            coord = coordinates[idx]
            score = sum(self.get_scores(
                image_candidate,
                kwargs.get("image").copy()
            ))
            scores.append([
                coord,
                score
            ])
        return {
            "scores": scores,
        }
    def __str__(self):
        return f"Location Ranker"
