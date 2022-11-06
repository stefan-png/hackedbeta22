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
turn = WHITE
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

                # if selected_tile != 0:
                #     print(Eval.possible_moves(grid, flipxy(selected_tile)))
                #     print(check_if_possible_move(grid, flipxy(selected_tile), flipxy(picked_pos)))
                #     print(picked_pos)
               
                if selected_tile == 0 or grid[flipxy(selected_tile)] == 0:
                    # we havent selected a tile yet, select one
                    selected_tile = picked_pos
                elif picked_pos == selected_tile:
                    # we picked the same as is selected
                    selected_tile = 0
                elif check_if_possible_move(grid, flipxy(selected_tile), flipxy(picked_pos)):
                    
                    # we picked a different tile than is selected
                    # if its a valid move, make the move
                    # TODO check if its my turn
                    grid[picked_pos[1], picked_pos[0]] = grid[selected_tile[1], selected_tile[0]]
                    grid[selected_tile[1], selected_tile[0]] = 0
                    selected_tile = 0
                else:
                    # otherwise, its an invalid move, select the picked tile
                    selected_tile = picked_pos

                # if we picked a tile, and we cant move there, select it.
                """
                if not Eval.check_on_board(flipxy(picked_pos)):
                    selected_tile = 0
                    continue
                # can assume user clicked on valid tile
 
                if selected_tile != 0:
                    # if selection is a valid tile
                        
                    if selected_tile == picked_pos: 
                        # clicked on selected tile, toggle the selected tile
                        selected_tile = 0
                    elif Eval.check_If_Valid(grid, flipxy(picked_pos), flipxy(selected_tile)):
                        # try to snap to picked pos
                        # TODO check if move is enemy, add point, etc etc
                        grid[picked_pos[1], picked_pos[0]] = grid[selected_tile[1], selected_tile[0]]
                        grid[selected_tile[1], selected_tile[0]] = 0
                        selected_tile = 0
                    else:
                        # attempted move is invalid.
                        selected_tile = 0
                    
                else:
                    # didn't have any point selected, select this square
                    selected_tile = picked_pos
                    if grid[picked_pos[1], picked_pos[0]] not in [0, 1]:
                        # check if picked pos has a piece on it. if so, hold it
                        held_piece = grid[picked_pos[1], picked_pos[0]]
                        held_peice_last_pos = picked_pos
                        grid[picked_pos[1], picked_pos[0]] = 0
                    else:
                        # if picked pos has no piece, reset hold variables
                        held_piece = 0
                        held_peice_last_pos = 0
                        """
            if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.WINDOWLEAVE:            
                #check if on board
                # if user released mouse on selected tile, unselect it and do nothing else
                if held_peice_last_pos == 0:
                    continue

                # if user released mouse 
                """

                if Eval.check_on_board(flipxy(picked_pos)) and Eval.check_If_Valid(grid, flipxy(picked_pos), flipxy(selected_tile)):

                    # dragged to valid tile, move the piece
                    grid[picked_pos[1], picked_pos[0]] = held_piece
                    

                else:
                    # dragged to invalid square, replace the piece
                    grid[held_peice_last_pos[1], held_peice_last_pos[0]] = held_piece
                
                if held_peice_last_pos != picked_pos:
                    selected_tile = 0

                held_piece = 0
                held_peice_last_pos = 0
                """

        # highlight whichever tile is selected
        if selected_tile != 0:
            g.draw_hex(surface, numpy.add(axial.axial_to_screen(selected_tile, scale), peter_offset), scale, (230, 230, 120))


        # draw whatever the player is holding
        if held_piece != 0 and held_piece.type != NONE:
            g.draw_piece(surface, spritesheet, mousepos, scale, held_piece.type, held_piece.colour)

        # draw all possible moves for selected piece
        if selected_tile != 0 and grid[selected_tile[1], selected_tile[0]] not in [0, 1]:
            # draw dot on each possible move
            for move in Eval.possible_moves(grid, (selected_tile[1], selected_tile[0])):
                pygame.draw.circle(surface, g.get_hex_colour(move[1], move[0]+2), numpy.add(axial.axial_to_screen((move[1], move[0]), scale), peter_offset), scale/3)

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

        # do the transparent stuff maybe 
        pygame.display.flip()