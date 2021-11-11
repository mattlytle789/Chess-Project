import numpy as np

# Parent class for all pieces
class Piece():
    # initializing the piece
    def __init__(self, currentSpace, type, color, label):
        self.availableSpaces = []
        self.currentSpace = currentSpace
        self.type = type
        self.color = color
        self.label = label
        self.hasMoved = False
    


