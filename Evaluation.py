def check_If_Valid(pos,pos_start):  # checks if the position is valid
    object_start = grid(pos_start)
    object= grid(pos)
    if (0 > pos[0]) or (pos[0] > 10) or (0 > pos[1]) or (pos[1] > 10) or (pos[0] + pos[1] > 15) or (
            pos[0] + pos[1] < 5):
        return False
    elif object_pos != 0:
        if object.colour == object_start.colour:
            return false
    elif in_Check() == True:
        return false
    else:
        return True

def in_Check():
    return False
