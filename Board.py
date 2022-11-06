import numpy as np
from Peices import *

grid = np.ones(shape=(11, 11), dtype = object)
for q in range(0, 11):
    for r in range(0, 11):
        if q + r >= 5 and q + r <= 15:
            grid[q, r] = 0

def set_Up_Board(mode="glinski"):
    if mode == 'glinski': #placeholder make enum or whatever for glinski's
        # white bishops
        grid[10,5] = peices(BISHOP, WHITE)
        grid[9,5] = peices(BISHOP, WHITE)
        grid[8,5] = peices(BISHOP, WHITE)
        #white queen
        grid[10,4] = peices(QUEEN, WHITE)
        #white king
        grid[9,6] = peices(KING, WHITE)
        #white knights
        grid[10, 3] = peices(KNIGHT, WHITE)
        grid[8,7] = peices(KNIGHT, WHITE)
        #white rooks
        grid[10,2] = peices(ROOK, WHITE)
        grid[7,8] = peices(ROOK, WHITE)
        #white pawns
        grid[10,1] = peices(PAWN, WHITE)
        grid[9,2] = peices(PAWN, WHITE)
        grid[8,3] = peices(PAWN, WHITE)
        grid[7,4] = peices(PAWN, WHITE)
        grid[6,5] = peices(PAWN, WHITE)
        grid[6,6] = peices(PAWN, WHITE)
        grid[6,7] = peices(PAWN, WHITE)
        grid[6,8] = peices(PAWN, WHITE)
        grid[6,9] = peices(PAWN, WHITE)

        # white bishops
        grid[0, 5] = peices(BISHOP, BLACK)
        grid[1, 5] = peices(BISHOP, BLACK)
        grid[2, 5] = peices(BISHOP, BLACK)
        # white queen
        grid[1, 4] = peices(QUEEN, BLACK)
        # white king
        grid[0, 6] = peices(WHITE, BLACK)
        # white knights
        grid[2, 3] = peices(KNIGHT, BLACK)
        grid[0, 7] = peices(KNIGHT, BLACK)
        # white rooks
        grid[3, 2] = peices(ROOK, BLACK)
        grid[0, 8] = peices(ROOK, BLACK)
        # white pawns
        grid[10, 1] = peices(PAWN, BLACK)
        grid[9, 2] = peices(PAWN, BLACK)
        grid[8, 3] = peices(PAWN, BLACK)
        grid[7, 4] = peices(PAWN, BLACK)
        grid[6, 5] = peices(PAWN, BLACK)
        grid[6, 6] = peices(PAWN, BLACK)
        grid[6, 7] = peices(PAWN, BLACK)
        grid[6, 8] = peices(PAWN, BLACK)
        grid[6, 9] = peices(PAWN, BLACK)


    return grid

