import numpy as np
from Peices import *
def set_Up_Board(mode="glinski"): # creates board and peices for the starting position of the game
    #creates the a hexagonal 2 dimensional grid o fhte board
    output = np.ones(shape=(11, 11), dtype=object)
    for q in range(0, 11):
        for r in range(0, 11):
            if q + r >= 5 and q + r <= 15:
                output[q, r] = 0

    if mode == 'glinski': #glinski's set up of the board
        # white bishops
        output[10,5] = peices(BISHOP, WHITE)
        output[9,5] = peices(BISHOP, WHITE)
        output[8,5] = peices(BISHOP, WHITE)
        #white queen
        output[10,4] = peices(QUEEN, WHITE)
        #white king
        output[9,6] = peices(KING, WHITE)
        #white knights
        output[10, 3] = peices(KNIGHT, WHITE)
        output[8,7] = peices(KNIGHT, WHITE)
        #white rooks
        output[10,2] = peices(ROOK, WHITE)
        output[7,8] = peices(ROOK, WHITE)
        # white pawns
        output[10, 1] = peices(PAWN, WHITE)
        output[9, 2] = peices(PAWN, WHITE)
        output[8, 3] = peices(PAWN, WHITE)
        output[7, 4] = peices(PAWN, WHITE)
        output[6, 5] = peices(PAWN, WHITE)
        output[6, 6] = peices(PAWN, WHITE)
        output[6, 7] = peices(PAWN, WHITE)
        output[6, 8] = peices(PAWN, WHITE)
        output[6, 9] = peices(PAWN, WHITE)
        # black bishops
        output[0, 5] = peices(BISHOP, BLACK)
        output[1, 5] = peices(BISHOP, BLACK)
        output[2, 5] = peices(BISHOP, BLACK)
        # black queen
        output[1, 4] = peices(QUEEN, BLACK)
        # black king
        output[0, 6] = peices(KING, BLACK)
        # black knights
        output[2, 3] = peices(KNIGHT, BLACK)
        output[0, 7] = peices(KNIGHT, BLACK)
        # black rooks
        output[3, 2] = peices(ROOK, BLACK)
        output[0, 8] = peices(ROOK, BLACK)
        #black pawns
        output[4, 1] = peices(PAWN, BLACK)
        output[4, 2] = peices(PAWN, BLACK)
        output[4, 3] = peices(PAWN, BLACK)
        output[4, 4] = peices(PAWN, BLACK)
        output[4, 5] = peices(PAWN, BLACK)
        output[3, 6] = peices(PAWN, BLACK)
        output[2, 7] = peices(PAWN, BLACK)
        output[1, 8] = peices(PAWN, BLACK)
        output[0, 9] = peices(PAWN, BLACK)

    return output