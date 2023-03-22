import numpy as np
from dataclasses import dataclass
from typing import List
from src.core.common.components.Grid import Grid

@dataclass
class Metadata:
    width: int
    height: int

@dataclass
class CandidateGenerationOutput:
    image: np.array
    grid_candidates: Grid # contains multiple cells
    metadata: Metadata
    

