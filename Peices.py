from enum import Enum
class type(Enum):
    pawn = 1
    bishop = 2
    knight = 3
    rook = 4
    queen = 5
    king = 6

class colour(Enum):
    white = 1
    black = 0

class peices:
    def __init__(self, type, colour):
        self.type = type
        self.colour = colour


