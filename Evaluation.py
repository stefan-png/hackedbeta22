import numpy as np
from Board import *
from Movment import *

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
        else:
            return None
    if in_Check(grid, pos, pos_start) == True:
        return False

    return True

def check_If_Valid_Check(grid, np_pos,np_pos_start):
    pos_start = (np_pos_start[0], np_pos_start[1])
    pos = (np_pos[0], np_pos[1])
    object_start = grid[pos_start]

    if object_start in [0, 1]:
        return False

    if not check_on_board(pos):
        return False
    object_pos = grid[pos[0], pos[1]]
    if object_pos not in [0, 1] and pos != pos_start:
        if object_pos.colour == object_start.colour:
            return False
        else:
            return None

    return True
def king_position(grid, pos_start, colour):
    for q in range(0, 11):
        for r in range(0, 11):
            if grid[q,r] not in [0, 1]:
                if grid[q,r].type == KING and grid[q,r].colour == colour:
                    coords = (q,r)
                    print(coords)
    return coords
    print('mistake')

def in_Check(grid, pos_c, pos_start):
    P_moves = []
    grid_sim = set_Up_Board(mode = 'blank')
    for q in range(0, 11):
        for r in range(0, 11):
            if grid[q, r] not in [0, 1]:
                grid_sim[q,r] = grid[q,r]
    grid_sim[pos_c] = grid[pos_start]
    grid_sim[pos_start] = 0
    #print([pos_c,grid_sim[pos_c].type])
    colour = grid[pos_start].colour
    king_pos = king_position(grid_sim, pos_start, colour)

    for q in range(0, 11):
        for r in range(0, 11):
             if grid_sim[q,r] not in [0, 1]:
                 if grid_sim[q,r].colour != grid_sim[king_pos]:
                    P_moves = P_moves + possible_moves(grid_sim, (q,r), c=1)

    for i in P_moves:
            pos = (i[0], i[1])
            if pos == king_pos:
                return True
    return False

def king(grid, pos, c=0): # returns list of all possible king moves
    moves = []
    m = [(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0),(0,1),(0,-1),(2,-1),(-2,1),(1,-2),(-1,2)]
    for i in m:
        if c == 0:
            if check_If_Valid(grid, np.add(pos,i), pos) == True or None:
                moves.append(np.add(pos,i))
        else:
            if check_If_Valid_Check(grid, np.add(pos,i), pos) == True or None:
                moves.append(np.add(pos,i))

    disp(pos, moves)
    return moves

def rook(grid, pos, c=0): # returns list of all possible rook moves
        moves = [pos]
        if c ==0:
            while check_If_Valid(grid, moves[-1], pos) == True:
                moves.append(np.add(moves[-1], (0,1)))
            if check_If_Valid(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid(grid, moves[-1], pos) == True:
                moves.append(np.subtract(moves[-1],(0,1)))
            if check_If_Valid(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid(grid, moves[-1], pos) == True:
                moves.append(np.add(moves[-1],(1,0)))
            if check_If_Valid(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid(grid, moves[-1], pos) == True:
                moves.append(np.subtract(moves[-1],(1,0)))
            if check_If_Valid(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid(grid, moves[-1], pos) == True:
                moves.append(np.add(moves[-1], (1, -1)))
            if check_If_Valid(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid(grid, moves[-1], pos) == True :
                moves.append(np.add(moves[-1], (-1, 1)))
            if check_If_Valid(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)
        else:
            while check_If_Valid_Check(grid, moves[-1], pos) == True:
                moves.append(np.add(moves[-1], (0, 1)))
            if check_If_Valid_Check(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid_Check(grid, moves[-1], pos) == True:
                moves.append(np.subtract(moves[-1], (0, 1)))
            if check_If_Valid_Check(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid_Check(grid, moves[-1], pos) == True:
                moves.append(np.add(moves[-1], (1, 0)))
            if check_If_Valid_Check(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid_Check(grid, moves[-1], pos) == True:
                moves.append(np.subtract(moves[-1], (1, 0)))
            if check_If_Valid_Check(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid_Check(grid, moves[-1], pos) == True:
                moves.append(np.add(moves[-1], (1, -1)))
            if check_If_Valid_Check(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

            while check_If_Valid_Check(grid, moves[-1], pos) == True:
                moves.append(np.add(moves[-1], (-1, 1)))
            if check_If_Valid_Check(grid, moves[-1], pos) != None:
                moves[-1] = pos
            else:
                moves.append(pos)

        disp(pos, moves)
        return moves

def bishop(grid, pos, c=0): # returns list of all possible bishop moves
    moves = [pos]
    if c == 0:
        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (1,1)))
        if check_If_Valid(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1], (1,1)))
        if check_If_Valid(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (1,-2)))
        if check_If_Valid(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1], (1,-2)))
        if check_If_Valid(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (2,-1)))
        if check_If_Valid(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid(grid, moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1], (2,-1)))
        if check_If_Valid(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)
    else:
        while check_If_Valid_Check(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (1,1)))
        if check_If_Valid_Check(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid_Check(grid, moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1], (1,1)))
        if check_If_Valid_Check(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid_Check(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (1,-2)))
        if check_If_Valid_Check(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid_Check(grid, moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1], (1,-2)))
        if check_If_Valid_Check(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid_Check(grid, moves[-1], pos) == True:
            moves.append(np.add(moves[-1], (2,-1)))
        if check_If_Valid_Check(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

        while check_If_Valid_Check(grid, moves[-1], pos) == True:
            moves.append(np.subtract(moves[-1], (2,-1)))
        if check_If_Valid_Check(grid, moves[-1], pos) != None:
            moves[-1] = pos
        else:
            moves.append(pos)

    disp(pos, moves)

    return moves

def knight(grid, pos, c=0): # returns list of all possible knight moves
    moves = [pos]
    m = [(1,-3),(-1,-2),(-2,-1),(-3,1),(-3,2),(-2,3),(-1,3),(1,2),(2,1),(3,-1),(3,-2),(2,-3)]
    for i in m:
        if c == 0:
            if check_If_Valid(grid, np.add(pos,i), pos) == True or None:
                moves.append(np.add(pos,i))
        else:
            if check_If_Valid_Check(grid, np.add(pos,i), pos) == True or None:
                moves.append(np.add(pos,i))

    disp(pos, moves)
    return moves

def pawn(grid, pos, c=0):
    moves = []
    posy = (pos[0], pos[1])
    r_grid = set_Up_Board()

    if c == 0:
        if grid[posy].colour == WHITE:
            if check_If_Valid(grid, np.subtract(pos, (1,0)), pos) == True:
              moves.append(np.subtract(pos, (1, 0)))
            if grid[(np.add((-1,-1),pos)[0] , np.add((-1,-1),pos)[1])] not in [1,0]:
                if grid[(np.add((-1, -1), pos)[0], np.add((-1, -1), pos)[1])].colour == BLACK:
                    if check_If_Valid(grid, np.add((-1, -1), pos), pos) == None:
                        moves.append(np.add((-1, -1), pos))
                        print('yes')
            if grid[(np.add((-2,1),pos)[0] , np.add((-2,1),pos)[1])] not in [1,0]:
                if grid[(np.add((-2,1), pos)[0], np.add((-2,1), pos)[1])].colour == BLACK:
                    if check_If_Valid(grid, np.add((-2,1), pos), pos) == None:
                        print('yes')
                        moves.append(np.add((-2,1), pos))
            if r_grid[posy] not in [0,1]:
                if grid[posy].type == r_grid[posy].type and grid[posy].colour == grid[posy].colour:
                    if check_If_Valid(grid, np.subtract(pos, (1,0)), pos) == True:
                        if check_If_Valid(grid, np.subtract(pos, (2, 0)), pos) == True:
                            moves.append(np.subtract(pos, (2, 0)))
        else:
            if check_If_Valid(grid, np.add(pos, (1,0)), pos) == True:
              moves.append(np.add(pos, (1, 0)))
            if grid[(np.subtract((-1,-1),pos)[0] , np.subtract((-1,-1),pos)[1])] not in [1,0]:
                if grid[(np.subtract((-1, -1), pos)[0], np.subtract((-1, -1), pos)[1])].colour == WHITE:
                    if check_If_Valid(grid, np.subtract((-1, -1), pos), pos) == None:
                        moves.append(np.subtract((-1, -1), pos))
                        print('yes')
            if grid[(np.subtract((-2,1),pos)[0] , np.subtract((-2,1),pos)[1])] not in [1,0]:
                if grid[(np.subtract((-2,1), pos)[0], np.subtract((-2,1), pos)[1])].colour == WHITE:
                    if check_If_Valid(grid, np.subtract((-2,1), pos), pos) == None:
                        print('yes')
                        moves.append(np.subtract((-2,1), pos))
            if r_grid[posy] not in [0,1]:
                if grid[posy].type == r_grid[posy].type and grid[posy].colour == grid[posy].colour:
                    if check_If_Valid(grid, np.add(pos, (1,0)), pos) == True:
                        if check_If_Valid(grid, np.add(pos, (2, 0)), pos) == True:
                            moves.append(np.add(pos, (2, 0)))

    return moves

def queen(grid, pos, c=0): # retunrs list of all possible queen moves
    moves = rook(grid, pos, c) + bishop(grid, pos, c)
    disp(pos,moves)
    return moves

def disp(pos, moves,c=0): # diplays the possible moves on a terminal grid
    output = np.ones(shape= (11,11))
    for q in range(0,11):
        for r in range(0,11):
            if q + r >= 5 and q + r <= 15:
                output[q,r] = 0

    for i in range(0,len(moves)):
        output[(moves[i][0],moves[i][1])] = 2
        output[(pos[0],pos[1])] = 9

   # print(output)

def possible_moves(grid, pos, c=0):
    if grid[pos].type == ROOK:
        return rook(grid, np.array(pos), c)
    elif grid[pos].type == BISHOP:
        return bishop(grid, np.array(pos), c)
    elif grid[pos].type == PAWN:
        return pawn(grid, np.array(pos), c)
    elif grid[pos].type == KING:
        return king(grid, np.array(pos), c)
    elif grid[pos].type == QUEEN:
        return queen(grid, np.array(pos), c)
    elif grid[pos].type == KNIGHT:
        return knight(grid, np.array(pos), c)
    else:
        print('error in possible moves, invalid type')
        return []

