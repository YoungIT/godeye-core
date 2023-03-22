from abc import ABC, abstractmethod

class Grid:
    def __init__(self, preload=True):
        self.cells = {}
        self.num_classes = 0

        if preload:
            self.load_cell_info()

    @abstractmethod
    def load_cell_info(self):
        """
        This function loads the cell info to self.cells.
        self.cells would be a map(id->value) of supported class for the classification problem
        """
        pass

    def add_class(self, value):
        self.cells[self.num_classes] = value
        self.num_classes += 1

    def get_cells(self):
        return list(self.cells.values())