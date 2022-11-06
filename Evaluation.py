import numpy as np
from Board import *


grid = set_Up_Board(mode = 'glinski')

def check_If_Valid(np_pos,np_pos_start):# checks if the position is valid
    pos_start = (np_pos_start[0],np_pos_start[1])
    pos = (np_pos[0],np_pos[1])
    object_start = grid[pos_start]
    if (0 > pos[0]) or (pos[0] > 10) or (0 > pos[1]) or (pos[1] > 10) or (pos[0] + pos[1] > 15) or (pos[0] + pos[1] < 5):
        return False
    object_pos = grid[pos]
    if object_pos != 0 and pos != pos_start:
        if object_pos.colour == object_start.colour:
            return False
    elif in_Check() == True:
        return False
    else:
        return True

def in_Check():
    return False
