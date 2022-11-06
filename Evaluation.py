from Board import *

grid = set_Up_Board(mode= 'glinski')

def check_If_Valid(pos,pos_start):  # checks if the position is valid
    object_start = grid[pos_start]
    if (0 > pos[0]) or (pos[0] > 10) or (0 > pos[1]) or (pos[1] > 10) or (pos[0] + pos[1] > 15) or (
            pos[0] + pos[1] < 5):
        return False

    object_pos = grid[pos]

    if type(object_pos) == object:
        if object_pos.colour == object_start.colour:
            return false
    elif in_Check() == True:
        return false
    else:
        return True

def in_Check():
    return False
