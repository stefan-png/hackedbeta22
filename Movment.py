import numpy as np
import Evaluation

def king(pos): # returns list of all possible king moves
    moves = []
    m = [(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0),(0,1),(0,-1),(2,-1),(-2,1),(1,-2),(-1,2)]
    for i in m:
        if check_If_Valid(np.add(pos,i), grid(pos)) == True:
            moves.append(np.add(pos,i))
    disp(pos, moves)
    return moves

def rook(pos): # returns list of all possible rook moves
        moves = [pos]

        while check_If_Valid(moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (0,1)))
        moves[-1] = pos

        while check_If_Valid(moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1],(0,1)))
        moves[-1] = pos

        while check_If_Valid(moves[-1], pos) == True:
            moves.append(np.add(moves[-1],(1,0)))
        moves[-1] = pos

        while check_If_Valid(moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1],(1,0)))
        moves[-1] = pos

        while check_If_Valid(moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (1, -1)))
        moves[-1] = pos

        while check_If_Valid(moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (-1, 1)))
        moves[-1] = pos

        disp(pos, moves)
        return moves

def bishop(pos): # returns list of all possible bishop moves
    moves = [pos]

    while check_If_Valid(moves[-1], pos) == True:
        moves.append(np.add(moves[-1], (1,1)))
    moves[-1] = pos

    while check_If_Valid(moves[-1], pos) == True:
        moves.append(np.subtract(moves[-1], (1,1)))
    moves[-1] = pos

    while check_If_Valid(moves[-1], pos) == True:
        moves.append(np.add(moves[-1], (1,-2)))
    moves[-1] = pos

    while check_If_Valid(moves[-1], pos) == True:
        moves.append(np.subtract(moves[-1], (1,-2)))
    moves[-1] = pos

    while check_If_Valid(moves[-1], pos) == True:
        moves.append(np.add(moves[-1], (2,-1)))
    moves[-1] = pos

    while check_If_Valid(moves[-1], pos) == True:
        moves.append(np.subtract(moves[-1], (2,-1)))
    moves[-1] = pos

    disp(pos, moves)
    return moves

def knight(pos): # returns list of all possible knight moves
    moves = [pos]
    m = [(1,-3),(-1,-2),(-2,-1),(-3,1),(-3,2),(-2,3),(-1,3),(1,2),(2,1),(3,-1),(3,-2),(2,-3)]
    for i in m:
        if check_If_Valid(np.add(pos,i), pos) == True:
            moves.append(np.add(pos,i))
    disp(pos, moves)
    return moves

def queen(pos): # retunrs list of all possible queen moves
    moves = rook(pos) + bishop(pos)
    disp(pos,moves)
    return moves

def disp(pos, moves): # diplays the possible moves on a terminal grid
    grid = np.ones(shape= (11,11))
    for q in range(0,11):
        for r in range(0,11):
            if q + r >= 5 and q + r <= 15:
                grid[q,r] = 0

    for i in range(0,len(moves)):
        grid[(moves[i][0],moves[i][1])] = 2
        grid[(pos[0],pos[1])] = 9

    print(grid)

