from abc import ABC, abstractmethod

class GridCell:
    def __init__(self, name, obj = None):
        self.name = name
        self.obj = obj