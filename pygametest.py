import sys, pygame, math
import numpy
import axial, graphics as g
import Evaluation as Eval
from Board import *

def flipxy(tuple):
    return (tuple[1], tuple[0])

def check_if_possible_move(grid, startpos, endpos):
    for move in Eval.possible_moves(grid, startpos):
        if tuple(move) == endpos:
            return True
    return False

screen_width = 800
screen_height = 800
origin = (screen_width/2, screen_height/2)

# setup board
grid = set_Up_Board()
turn = BLACK # WHITE
print(Eval.check_If_Valid(grid, (4,4), (10,4)))
if __name__=="__main__":

    pygame.init()
    surface = pygame.display.set_mode((screen_width, screen_height))

    spritesheet = g.load_spritesheet("chesspieces.png")
    font = pygame.font.SysFont(None, 24)

    #piece currently held by player's cursor
    held_piece = 0
    held_peice_last_pos = (0, 0)

    selected_tile = NONE

    captured_white_pieces = numpy.zeros(7)
    captured_black_pieces = numpy.zeros(7)

    # game loop
    while True:

        # state
        scale = 35

        # draw background
        surface.fill((255, 255, 255, 255))
        g.draw_board(surface, origin, scale)

        mousepos = pygame.mouse.get_pos()

        peter_offset = ( (screen_width-15*scale)/2, (screen_height-15*math.sqrt(3)*scale)/2 )

        picked_pos = axial.axial_round(axial.screen_to_axial(numpy.subtract(mousepos, peter_offset), scale))
        pos = numpy.add(axial.axial_to_screen(picked_pos, scale), peter_offset)
        g.draw_hex(surface, pos, scale, (230, 230, 240), 4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                # make sure the picked_pos is on the board
                if not Eval.check_on_board(flipxy(picked_pos)):
                    selected_tile = 0
                    continue

                if selected_tile == 0 or grid[flipxy(selected_tile)] == 0:
                    # we havent selected a tile yet, select one
                    selected_tile = picked_pos
                elif picked_pos == selected_tile:
                    # we picked the same as is selected
                    selected_tile = 0
                elif check_if_possible_move(grid, flipxy(selected_tile), flipxy(picked_pos)) and grid[flipxy(selected_tile)].colour == turn:
                    
                    # we picked a different tile than is selected
                    # if its a valid move, make the move

                    # TODO if we are going to eat an enemy piece, move it to the side.
                    piece_idx = NONE
                    if grid[flipxy(picked_pos)] not in [0, 1]:
                        piece_idx = grid[flipxy(picked_pos)].type
                    if turn == WHITE:
                        turn = BLACK
                        captured_black_pieces[piece_idx] += 1
                        print("taken black pieces", captured_black_pieces)
                    else:
                        turn = WHITE
                        captured_white_pieces[piece_idx] += 1
                        print("taken white pieces", captured_white_pieces)

                    grid[picked_pos[1], picked_pos[0]] = grid[selected_tile[1], selected_tile[0]]
                    grid[selected_tile[1], selected_tile[0]] = 0
                    selected_tile = 0
                else:
                    # otherwise, its an invalid move, select the picked tile
                    selected_tile = picked_pos

            if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.WINDOWLEAVE:            
                #check if on board
                # if user released mouse on selected tile, unselect it and do nothing else
                if held_peice_last_pos == 0:
                    continue

                # if user released mouse 
        
        # *** end event handling ***

        # highlight whichever tile is selected
        if selected_tile != 0:
            g.draw_hex(surface, numpy.add(axial.axial_to_screen(selected_tile, scale), peter_offset), scale, (230, 230, 120))


        # draw whatever the player is holding
        if held_piece != 0 and held_piece.type != NONE:
            g.draw_piece(surface, spritesheet, mousepos, scale, held_piece.type, held_piece.colour)

        # draw all possible moves for selected piece
        if selected_tile != 0 and grid[selected_tile[1], selected_tile[0]] not in [0, 1] and grid[flipxy(selected_tile)].colour == turn:
            # draw dot on each possible move
            for move in Eval.possible_moves(grid, (selected_tile[1], selected_tile[0])):
                pygame.draw.circle(surface, g.get_hex_colour(move[1], move[0]+2), numpy.add(axial.axial_to_screen((move[1], move[0]), scale), peter_offset), scale*g.SQRT32/2)

        # draw debug text
        img = font.render("hovering: " + str(picked_pos), True, (1,1,1))
        surface.blit(img, (20, 20))

        # draw board
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[x,y] in [0, 1]:
                    continue
                piece = grid[x, y].type
                colour = grid[x, y].colour
                g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((y, x), scale), peter_offset), scale, piece, colour)

        # draw piece held in cursor


        # draw the captured pieces
        whitey = 0
        for i in range(1, len(captured_white_pieces)):
            for piece in range(int(captured_white_pieces[i])):
                g.draw_piece(surface, spritesheet, (origin[0]-9.5 * scale, origin[1]-7.5*scale + whitey * scale), scale, i, WHITE)
                whitey += 1
         # draw the captured pieces
        blacky = 0
        for i in range(1, len(captured_black_pieces)):
            for piece in range(int(captured_black_pieces[i])):
                g.draw_piece(surface, spritesheet, (origin[0]+9.5 * scale, origin[1]-7.5*scale + blacky * scale), scale, i, BLACK)
                blacky += 1
            


        # do the transparent stuff maybe 
        pygame.display.flip()