import numpy as np
from Board import *

# checks if agiven position would be on the board
def check_on_board(pos):
    return pos[0] >= 0 and pos[0] < 11 and pos[1] >= 0 and pos[1] < 11 and (pos[0] + pos[1] <= 15) and (pos[0] + pos[1] >= 5)

def check_If_Valid(grid, np_pos,np_pos_start):# checks if the position is valid

    pos_start = (np_pos_start[0],np_pos_start[1])
    pos = (np_pos[0],np_pos[1])
    object_start = grid[pos_start]

    if object_start in [0, 1]:
        return False

    if not check_on_board(pos):
        return False
    object_pos = grid[pos[0], pos[1]]
    if object_pos not in [0, 1] and pos != pos_start:
        if object_pos.colour == object_start.colour:
            return False
    elif in_Check() == True:
        return False
    else:
        return True

def in_Check():
    return False
