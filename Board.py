import numpy as np
from Peices import *
def set_Up_Board(mode="glinski"): # creates board and peices for the starting position of the game
    #creates the a hexagonal 2 dimensional grid o fhte board
    grid = np.ones(shape=(11, 11), dtype=object)
    for q in range(0, 11):
        for r in range(0, 11):
            if q + r >= 5 and q + r <= 15:
                grid[q, r] = 0

    if mode == 'glinski': #glinski's set up of the board
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
        # white pawns
        grid[10, 1] = peices(PAWN, WHITE)
        grid[9, 2] = peices(PAWN, WHITE)
        grid[8, 3] = peices(PAWN, WHITE)
        grid[7, 4] = peices(PAWN, WHITE)
        grid[6, 5] = peices(PAWN, WHITE)
        grid[6, 6] = peices(PAWN, WHITE)
        grid[6, 7] = peices(PAWN, WHITE)
        grid[6, 8] = peices(PAWN, WHITE)
        grid[6, 9] = peices(PAWN, WHITE)
        # black bishops
        grid[0, 5] = peices(BISHOP, BLACK)
        grid[1, 5] = peices(BISHOP, BLACK)
        grid[2, 5] = peices(BISHOP, BLACK)
        # black queen
        grid[1, 4] = peices(QUEEN, BLACK)
        # black king
        grid[0, 6] = peices(WHITE, BLACK)
        # black knights
        grid[2, 3] = peices(KNIGHT, BLACK)
        grid[0, 7] = peices(KNIGHT, BLACK)
        # black rooks
        grid[3, 2] = peices(ROOK, BLACK)
        grid[0, 8] = peices(ROOK, BLACK)
        #black pawns
        grid[4, 1] = peices(PAWN, BLACK)
        grid[4, 2] = peices(PAWN, BLACK)
        grid[4, 3] = peices(PAWN, BLACK)
        grid[4, 4] = peices(PAWN, BLACK)
        grid[4, 5] = peices(PAWN, BLACK)
        grid[3, 6] = peices(PAWN, BLACK)
        grid[2, 7] = peices(PAWN, BLACK)
        grid[1, 8] = peices(PAWN, BLACK)
        grid[0, 9] = peices(PAWN, BLACK)

    return grid