from typing import List

import torch
import numpy as np
from transformers import CLIPProcessor, CLIPModel

class StreetClipGenerator():
    def __init__(self, model_name, use_torch_compiled):
        self.model = CLIPModel.from_pretrained(model_name)
        self.processor = CLIPProcessor.from_pretrained(model_name)

        if(use_torch_compiled):
            self.model = torch.compile(self.model)

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