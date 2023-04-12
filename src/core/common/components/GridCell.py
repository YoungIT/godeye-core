from abc import ABC, abstractmethod
from typing import Tuple, List

class GridCell:
    def __init__(self, name: str, repr_cls = None, coordinate: Tuple[float, float] = None, childs: List = []):
        self.repr_cls = repr_cls # class represent for this grid (Country, City)
        self.name = name
        self.coordinate = coordinate
        self.childs = childs