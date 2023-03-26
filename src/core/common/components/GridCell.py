from abc import ABC, abstractmethod
from typing import Tuple, List

class GridCell:
    def __init__(self, name: str, coordinate: Tuple[float, float] = None, childs: List = []):
        self.name = name
        self.coordinate = coordinate
        self.childs = childs