import numpy as np
from Peices import *

grid = np.ones(shape=(11, 11), dtype = object)
for q in range(0, 11):
    for r in range(0, 11):
        if q + r >= 5 and q + r <= 15:
            grid[q, r] = 0

def set_Up_Board(mode):
    if mode == 'glinski': #placeholder make enum or whatever for glinski's
        # white bishops
        grid[10,5] = peices(type(2), colour(1))
        grid[9,5] = peices(type(2), colour(1))
        grid[8,5] = peices(type(2), colour(1))
        #white queen
        grid[10,4] = peices(type(5), colour(1))
        #white king
        grid[9,6] = peices(type(6), colour(1))
        #white knights
        grid[10, 3] = peices(type(3), colour(1))
        grid[8,7] = peices(type(3), colour(1))
        #white rooks
        grid[10,2] = peices(type(4), colour(1))
        grid[7,8] = peices(type(4), colour(1))
        #white pawns
        grid[10,1] = peices(type(4), colour(1))
        grid[9,2] = peices(type(4), colour(1))
        grid[8,3] = peices(type(4), colour(1))
        grid[7,4] = peices(type(4), colour(1))
        grid[6,5] = peices(type(4), colour(1))
        grid[6,6] = peices(type(4), colour(1))
        grid[6,7] = peices(type(4), colour(1))
        grid[6,8] = peices(type(4), colour(1))
        grid[6,9] = peices(type(4), colour(1))
        # black bishops
        grid[0, 5] = peices(type(2), colour(0))
        grid[1, 5] = peices(type(2), colour(0))
        grid[2, 5] = peices(type(2), colour(0))
        # black queen
        grid[1, 4] = peices(type(5), colour(0))
        # black king
        grid[0, 6] = peices(type(6), colour(0))
        # black knights
        grid[2, 3] = peices(type(3), colour(0))
        grid[0, 7] = peices(type(3), colour(0))
        # black rooks
        grid[3, 2] = peices(type(4), colour(0))
        grid[0, 8] = peices(type(4), colour(0))
        # black pawns
        grid[4, 1] = peices(type(4), colour(0))
        grid[4, 2] = peices(type(4), colour(0))
        grid[4, 3] = peices(type(4), colour(0))
        grid[4, 4] = peices(type(4), colour(0))
        grid[4, 5] = peices(type(4), colour(0))
        grid[3, 6] = peices(type(4), colour(0))
        grid[2, 7] = peices(type(4), colour(0))
        grid[1, 8] = peices(type(4), colour(0))
        grid[0, 9] = peices(type(4), colour(0))

set_Up_Board('glinski')
print(grid)
