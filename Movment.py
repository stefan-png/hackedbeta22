import numpy as np
from Evaluation import *

def king(grid, pos): # returns list of all possible king moves
    moves = []
    m = [(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0),(0,1),(0,-1),(2,-1),(-2,1),(1,-2),(-1,2)]
    for i in m:
        if check_If_Valid(grid, np.add(pos,i), pos) == True:
            moves.append(np.add(pos,i))
    disp(pos, moves)
    return moves

def rook(grid, pos): # returns list of all possible rook moves
        moves = [pos]

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (0,1)))
        moves[-1] = pos

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1],(0,1)))
        moves[-1] = pos

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1],(1,0)))
        moves[-1] = pos

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1],(1,0)))
        moves[-1] = pos

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (1, -1)))
        moves[-1] = pos

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (-1, 1)))
        moves[-1] = pos

        disp(pos, moves)
        return moves

def bishop(grid, pos): # returns list of all possible bishop moves
    moves = [pos]

    while check_If_Valid(grid, moves[-1], pos) == True:
        moves.append(np.add(moves[-1], (1,1)))
    moves[-1] = pos

    while check_If_Valid(grid, moves[-1], pos) == True:
        moves.append(np.subtract(moves[-1], (1,1)))
    moves[-1] = pos

    while check_If_Valid(grid, moves[-1], pos) == True:
        moves.append(np.add(moves[-1], (1,-2)))
    moves[-1] = pos

    while check_If_Valid(grid, moves[-1], pos) == True:
        moves.append(np.subtract(moves[-1], (1,-2)))
    moves[-1] = pos

    while check_If_Valid(grid, moves[-1], pos) == True:
        moves.append(np.add(moves[-1], (2,-1)))
    moves[-1] = pos

    while check_If_Valid(grid, moves[-1], pos) == True:
        moves.append(np.subtract(moves[-1], (2,-1)))
    moves[-1] = pos

    disp(pos, moves)

    return moves

def knight(grid, pos): # returns list of all possible knight moves
    moves = [pos]
    m = [(1,-3),(-1,-2),(-2,-1),(-3,1),(-3,2),(-2,3),(-1,3),(1,2),(2,1),(3,-1),(3,-2),(2,-3)]
    for i in m:
        if check_If_Valid(grid, np.add(pos,i), pos) == True:
            moves.append(np.add(pos,i))
    disp(pos, moves)
    return moves

def pawn(grid, pos):
    moves = []
    return moves

def queen(grid, pos): # retunrs list of all possible queen moves
    moves = rook(grid, pos) + bishop(grid, pos)
    disp(pos,moves)
    return moves

def disp(pos, moves): # diplays the possible moves on a terminal grid
    output = np.ones(shape= (11,11))
    for q in range(0,11):
        for r in range(0,11):
            if q + r >= 5 and q + r <= 15:
                output[q,r] = 0

    for i in range(0,len(moves)):
        output[(moves[i][0],moves[i][1])] = 2
        output[(pos[0],pos[1])] = 9

    print(output)

def possible_moves(grid, pos):
    if grid[pos].type == ROOK:
        return rook(grid, np.array(pos))
    elif grid[pos].type == BISHOP:
        return bishop(grid, np.array(pos))
    elif grid[pos].type == PAWN:
        return pawn(grid, np.array(pos))
    elif grid[pos].type == KING:
        return king(grid, np.array(pos))
    elif grid[pos].type == QUEEN:
        return queen(grid, np.array(pos))
    elif grid[pos].type == KNIGHT:
        return knight(grid, np.array(pos))
    else:
        print('error in possible moves, invalid type')
        return []

# possible_moves((9,6))