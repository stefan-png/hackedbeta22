import numpy as np

def king(pos):
    moves = []
    m = [(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0),(0,1),(0,-1),(2,-1),(-2,1),(1,-2),(-1,2)]
    for i in m:
        if check_If_Valid(np.add(pos,i)) == True:
            moves.append(np.add(pos,i))
    disp(pos, moves)
    return moves

def rook(pos):
        moves = [pos]

        while check_If_Valid(moves[-1]) == True:
            moves.append(np.add(moves[-1], (0,1)))
        moves[-1] = pos

        while check_If_Valid(moves[-1]) == True:
            moves.append(np.subtract(moves[-1],(0,1)))
        moves[-1] = pos

        while check_If_Valid(moves[-1]) == True:
            moves.append(np.add(moves[-1],(1,0)))
        moves[-1] = pos

        while check_If_Valid(moves[-1]) == True:
            moves.append(np.subtract(moves[-1],(1,0)))
        moves[-1] = pos

        while check_If_Valid(moves[-1]) == True:
            moves.append(np.add(moves[-1], (1, -1)))
        moves[-1] = pos

        while check_If_Valid(moves[-1]) == True:
            moves.append(np.add(moves[-1], (-1, 1)))
        moves[-1] = pos

        disp(pos, moves)
        return moves

def bishop(pos):
    moves = [pos]

    while check_If_Valid(moves[-1]) == True:
        moves.append(np.add(moves[-1], (1,1)))
    moves[-1] = pos

    while check_If_Valid(moves[-1]) == True:
        moves.append(np.subtract(moves[-1], (1,1)))
    moves[-1] = pos

    while check_If_Valid(moves[-1]) == True:
        moves.append(np.add(moves[-1], (1,-2)))
    moves[-1] = pos

    while check_If_Valid(moves[-1]) == True:
        moves.append(np.subtract(moves[-1], (1,-2)))
    moves[-1] = pos

    while check_If_Valid(moves[-1]) == True:
        moves.append(np.add(moves[-1], (2,-1)))
    moves[-1] = pos

    while check_If_Valid(moves[-1]) == True:
        moves.append(np.subtract(moves[-1], (2,-1)))
    moves[-1] = pos

    disp(pos, moves)
    return moves

def knight(pos):
    moves = [pos]
    m = [(1,-3),(-1,-2),(-2,-1),(-3,1),(-3,2),(-2,3),(-1,3),(1,2),(2,1),(3,-1),(3,-2),(2,-3)]
    for i in m:
        if check_If_Valid(np.add(pos,i)) == True:
            moves.append(np.add(pos,i))
    disp(pos, moves)
    return moves

def queen(pos):
    moves = rook(pos) + bishop(pos)
    disp(pos,moves)
    return moves

def check_If_Valid(pos):
    if (0 > pos[0]) or (pos[0] > 10) or (0>pos[1]) or (pos[1] >10) or (pos[0] + pos[1] > 15) or (pos[0] + pos[1] < 5):
        return False
    else:
        return True

def disp(pos, moves):
    grid = np.ones(shape= (11,11))
    for q in range(0,11):
        for r in range(0,11):
            if q + r >= 5 and q + r <= 15:
                grid[q,r] = 0

    for i in range(0,len(moves)):
        grid[(moves[i][0],moves[i][1])] = 2
        grid[(pos[0],pos[1])] = 9

    print(grid)

queen([5,5])

