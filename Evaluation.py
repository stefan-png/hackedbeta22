import numpy as np
from Board import *
def bandaid(grid,moves,pos,c):
    # this prunes the moves output of our movments functionsto account for check convert coords into lists and remove origional position
    a = 0
    for i in moves:
        moves[a] = [i[0], i[1]]
        a = a + 1
    i = 0
    while i < len(moves):
        if moves[i][1] == pos[1] and moves[i][0] == pos[0]:
            moves.pop(i)
        else:
            i = i + 1
    checked_moves = []
    if c == 0 and get_piece_type_at(grid, (pos[0], pos[1])) != NONE:
        for i in moves:
            if in_Check(grid, (i[0], i[1]), (pos[0], pos[1])) == True:
                checked_moves.append(i)
        for i in checked_moves:
            moves.remove(i)
    return moves

# checks if agiven position would be on the board
def check_on_board(pos):
    return pos[0] >= 0 and pos[0] < 11 and pos[1] >= 0 and pos[1] < 11 and (pos[0] + pos[1] <= 15) and (pos[0] + pos[1] >= 5)

# returns the type of the piece at a given position
# if you query a tile which is off the board, or is empty, returns NONE
def get_piece_type_at(grid, pos):
    if (not check_on_board(pos)) or grid[pos] in [0, 1]:
        return NONE
    else:
        return grid[pos].type

#cause of check if valid result
No_Piece_Selcted = 0
Not_On_Board = 1
Same_Square = 2
Attacking_Same_Colour = 3
Attacking = 5
Blank_Square = 6

# checks if some move is valid
def check_If_Valid(grid, np_pos,np_pos_start):
    pos_start = (np_pos_start[0],np_pos_start[1])
    pos = (np_pos[0],np_pos[1])
    object_start = grid[pos_start]

    # is the peice selected a peice
    if get_piece_type_at(grid, pos_start) == NONE:
        return (False, No_Piece_Selcted)
    #is it on the board
    if not check_on_board(pos):
        return (False, Not_On_Board)
    # are you trying to move it to the same place
    if pos == pos_start:
        return (False, Same_Square)
    
    object_pos = grid[pos[0], pos[1]]
    if get_piece_type_at(grid, pos) != NONE:
        # try to move onto some other piece
        if object_pos.colour == object_start.colour:
            # if try to move onto own piece
            return (False, Attacking_Same_Colour)
        else:
            return (True, Attacking)

    # otherwise, tried to move onto some blank square
    return (True, Blank_Square)

def king_position(grid, colour):
    # returns position of king on grid for specific colour
    for q in range(0, 11):
        for r in range(0, 11):
            if grid[q,r] not in [0, 1]:
                if get_piece_type_at(grid, (q, r)) == KING and grid[q,r].colour == colour:
                    return (q,r)

    return (0, 0)

# checks if moving from pos_start to pos_c will put you in check
def in_Check(grid, pos_c, pos_start):
    P_moves = []

    if get_piece_type_at(grid, pos_start) == NONE:
        return False

    # copy the given grid
    grid_sim = set_Up_Board(mode = 2)
    for q in range(0, 11):
        for r in range(0, 11):
            # if grid[q, r] not in [0, 1]:
            grid_sim[q,r] = grid[q,r]

    # make the move on the simulated grid
    grid_sim[tuple(pos_c)] = grid_sim[tuple(pos_start)]
    grid_sim[tuple(pos_start)] = 0
        
    # color of the piece moved
    king_colour = grid_sim[pos_c].colour
    # position of king on simulated grid after making the simulated move
    king_pos = king_position(grid_sim, king_colour)

    if get_piece_type_at(grid, pos_start) == KING:
        king_colour = grid[tuple(pos_start)].colour
        king_pos = tuple(pos_c)

    # loop through each enemy piece and find its possible moves
    for q in range(0, 11):
        for r in range(0, 11):
             if get_piece_type_at(grid_sim, (q,r)) != NONE:
                 if grid_sim[q,r].colour != king_colour:
                    P_moves += possible_moves(grid_sim, (q,r), c=1)

    # are any of the enemy possible moves capturing the king?
    for move in P_moves:
        if tuple(move) == tuple(king_pos):
            return  True
        
    return False

def king(grid, pos, c=0): # returns list of all possible king moves
    moves = []
    m = [(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0),(0,1),(0,-1),(2,-1),(-2,1),(1,-2),(-1,2)]
    for i in m:
        if check_If_Valid(grid, np.add(pos,i), pos)[0] == True:
            moves.append(np.add(pos,i))

    return bandaid(grid,moves,pos,c)

def rook(grid, pos, c=0): # returns list possible rook moves
        moves = [pos]
        # moves in the positive y
        while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square, Same_Square):
            move = np.add(moves[-1], (0,1))
            moves.append(move)
        if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
            moves[-1] = pos
        else:
            moves.append(pos)
        #moves in the negative y
        while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square, Same_Square):
            move = np.subtract(moves[-1], (0, 1))
            moves.append(move)
        if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
            moves[-1] = pos
        else:
            moves.append(pos)
        #moves in the postiive x
        while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square, Same_Square):
            moves.append(np.add(moves[-1], (1,0)))
        if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
            moves[-1] = pos
        else:
            moves.append(pos)
        #moves in the negative x
        while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square, Same_Square):
            moves.append(np.subtract(moves[-1], (1,0)))
        if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
            moves[-1] = pos
        else:
            moves.append(pos)
        #moves in the positive z
        while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square, Same_Square):
            moves.append(np.add(moves[-1], (-1, 1)))
        if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
            moves[-1] = pos
        else:
            moves.append(pos)
        #moves in the negative y
        while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square, Same_Square):
            moves.append(np.subtract(moves[-1], (-1, 1)))
        if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
            moves[-1] = pos
        else:
            moves.append(pos)

        return bandaid(grid, moves, pos, c)

def bishop(grid, pos, c=0): # returns list of all possible bishop moves
    moves = [pos]
    while check_If_Valid(grid, moves[-1], pos)[1] in (Blank_Square,Same_Square):
        moves.append(np.add(moves[-1], (1,1)))
    if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
        moves[-1] = pos
    else:
        moves.append(pos)

    while check_If_Valid(grid, moves[-1], pos)[1] in (Blank_Square,Same_Square):
        moves.append(np.subtract(moves[-1], (1,1)))
    if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
        moves[-1] = pos
    else:
        moves.append(pos)

    while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square,Same_Square):
        moves.append(np.add(moves[-1], (1,-2)))
    if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
        moves[-1] = pos
    else:
        moves.append(pos)

    while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square,Same_Square):
        moves.append(np.subtract(moves[-1], (1,-2)))
    if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
        moves[-1] = pos
    else:
        moves.append(pos)

    while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square,Same_Square):
        moves.append(np.add(moves[-1], (2,-1)))
    if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
        moves[-1] = pos
    else:
        moves.append(pos)

    while check_If_Valid(grid, moves[-1], pos)[1]  in (Blank_Square,Same_Square):
        moves.append(np.subtract(moves[-1], (2,-1)))
    if check_If_Valid(grid, moves[-1], pos)[1] != Attacking:
        moves[-1] = pos
    else:
        moves.append(pos)

    return bandaid(grid,moves,pos,c)

def knight(grid, pos, c=0): # returns list of all possible knight moves
    moves = []
    m = [(1,-3),(-1,-2),(-2,-1),(-3,1),(-3,2),(-2,3),(-1,3),(1,2),(2,1),(3,-1),(3,-2),(2,-3)]
    for i in m:
        if check_If_Valid(grid, np.add(pos,i), pos)[0] == True:
            moves.append(np.add(pos,i))
    return bandaid(grid,moves,pos,c)

def pawn(grid, pos, c=0, r_grid = set_Up_Board(2)):
    moves = []
    posy = (pos[0], pos[1])

    #absolute spaghetti with a ton of redundency TODO prune this code
    if grid[posy].colour == WHITE:
        if check_If_Valid(grid, np.subtract(pos, (1,0)), pos)[0] == True and check_If_Valid(grid, np.subtract(pos, (1,0)), pos)[1] != Attacking:
          moves.append(np.subtract(pos, (1, 0)))
        if get_piece_type_at(grid, (pos[0]-1, pos[1]-1)) != NONE:
            if grid[(np.add((-1, -1), pos)[0], np.add((-1, -1), pos)[1])].colour == BLACK:
                if check_If_Valid(grid, np.add((-1, -1), pos), pos)[1] == Attacking:
                    moves.append(np.add((-1, -1), pos))
        if get_piece_type_at(grid, (pos[0]-2 , pos[1]+1)) != NONE:
            if grid[(np.add((-2,1), pos)[0], np.add((-2,1), pos)[1])].colour == BLACK:
                if check_If_Valid(grid, np.add((-2,1), pos), pos)[1] == Attacking:
                    moves.append(np.add((-2,1), pos))
        if r_grid[posy] not in [0,1]:
            if grid[posy].type == r_grid[posy].type and grid[posy].colour == grid[posy].colour:
                if check_If_Valid(grid, np.subtract(pos, (1,0)), pos)[0] == True and check_If_Valid(grid, np.subtract(pos, (1,0)), pos)[1] != Attacking:
                    if check_If_Valid(grid, np.subtract(pos, (2, 0)), pos)[0] == True and check_If_Valid(grid, np.subtract(pos, (2,0)), pos)[1] != Attacking:
                        moves.append(np.subtract(pos, (2, 0)))
    else:
        if check_If_Valid(grid, np.add(pos, (1,0)), pos)[0] == True and check_If_Valid(grid, np.add(pos, (1,0)), pos)[1] != Attacking:
          moves.append(np.add(pos, (1, 0)))
        if get_piece_type_at(grid, (pos[0]+1, pos[1]+1)) != NONE:
            if grid[(np.add((1,1), pos)[0], np.add((1,1), pos)[1])].colour == WHITE:
                if check_If_Valid(grid, np.add((1, 1), pos), pos)[1] == Attacking:
                    moves.append(np.add((1, 1), pos))

        if get_piece_type_at(grid, (pos[0]+2 , pos[1]-1)) != NONE:
            if grid[(np.add((2,-1), pos)[0], np.add((2,-1), pos)[1])].colour == WHITE:
                if check_If_Valid(grid, np.add((2,-1), pos), pos)[1] == Attacking:

                    moves.append(np.add((2,-1), pos))
        if r_grid[posy] not in [0,1]:
            if grid[posy].type == r_grid[posy].type and grid[posy].colour == grid[posy].colour:
                if check_If_Valid(grid, np.add(pos, (1,0)), pos)[0] == True and check_If_Valid(grid, np.add(pos, (1,0)), pos)[1] != Attacking:
                    if check_If_Valid(grid, np.add(pos, (2, 0)), pos)[0] == True and check_If_Valid(grid, np.add(pos, (2,0)), pos)[1] != Attacking:
                        moves.append(np.add(pos, (2, 0)))
    return bandaid(grid,moves,pos,c)

def queen(grid, pos, c=0): # retunrs list of all possible queen moves
    moves = rook(grid, pos, c) + bishop(grid, pos, c)
    return moves

def possible_moves(grid, pos, c=0, r_grid=set_Up_Board(2)): # returns list of all possible moves for a given tile
    if grid[pos].type == ROOK:
        return rook(grid, np.array(pos), c)
    elif grid[pos].type == BISHOP:
        return bishop(grid, np.array(pos), c)
    elif grid[pos].type == PAWN:
        return pawn(grid, np.array(pos), c, r_grid)
    elif grid[pos].type == KING:
        return king(grid, np.array(pos), c)
    elif grid[pos].type == QUEEN:
        return queen(grid, np.array(pos), c)
    elif grid[pos].type == KNIGHT:
        return knight(grid, np.array(pos), c)

def check_Mate(grid, colour): # checks if in check mate for a given colour
    moves = []
    for q in range(0, 11):
        for r in range(0, 11):
            if grid[q, r] not in [0, 1]:
                if grid[q,r].colour == colour:
                    moves = moves + possible_moves(grid, (q,r))
    if len(moves) == 0:
        return True
    else:
        return False

def promotable_Pawns(grid, colour): # checks if there are pawns to be promoted and then makes them queens if so
    # im assuming people would want queens so its defaulted to that thoguh it might be a good idea to add a selction screen for it
    if colour == WHITE:
        print('white')
        m = [(5,0),(4,1),(3,2),(2,3),(1,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)]
        for i in m:
            if get_piece_type_at(grid, i) == PAWN:
                if grid[i].colour == WHITE:
                    grid[i] = peices(QUEEN, WHITE)
    else:
        m = [(10,0),(10,1),(10,2),(10,3),(10,4),(10,5),(9,6),(8,7),(7,8),(6,9),(7,10)]
        for i in m:
            if get_piece_type_at(grid, i) == PAWN:
                if grid[i].colour == BLACK:
                    grid[i] = peices(QUEEN, BLACK)





