import sys, pygame, math
import numpy

import axial, graphics as g
from Board import *

screen_width = 800
screen_height = 800
origin = (screen_width/2, screen_height/2)

pygame.init()
surface = pygame.display.set_mode((screen_width, screen_height))

spritesheet = g.load_spritesheet("chesspieces.png")
font = pygame.font.SysFont(None, 24)
    
# setup board
grid = set_Up_Board()
turn = WHITE

#piece currently held by player's cursor
held_piece = peices(NONE, WHITE)
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

    # pygame.draw.circle(surface, (255, 255, 255), pos, scale/3)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if not (picked_pos[0] >= 0 and picked_pos[0] < 11 and picked_pos[0] >= 0 and picked_pos[1] < 11):
                continue

            
            if grid[picked_pos[1], picked_pos[0]] == 0:
                # TODO change to check for valid move
                if selected_tile != 0:
                    # try to snap to picked pos
                    grid[picked_pos[1], picked_pos[0]] = grid[selected_tile[1], selected_tile[0]]
                    grid[selected_tile[1], selected_tile[0]] = 0
                    selected_tile = 0
                    # make sure to reset any hold variables
                    held_piece = 0
                    held_peice_last_pos = (0, 0)
                else:
                    # didn't have any point selected, select this square
                    selected_tile = picked_pos

            elif grid[picked_pos[1], picked_pos[0]] not in [0, 1]:
                # picked a piece
                
                selected_tile = picked_pos
                held_piece = grid[picked_pos[1], picked_pos[0]]
                held_peice_last_pos = picked_pos
                grid[picked_pos[1], picked_pos[0]] = 0
                    
        if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.WINDOWLEAVE:            
            #check if on board
            if picked_pos[0] >= 0 and picked_pos[0] < 11 and picked_pos[0] >= 0 and picked_pos[1] < 11 and grid[picked_pos[1], picked_pos[0]] == 0:

                # dragged to valid tile, move the piece
                grid[picked_pos[1], picked_pos[0]] = held_piece
                

            else:
                # dragged to invalid square, replace the piece
                grid[held_peice_last_pos[1], held_peice_last_pos[0]] = held_piece
            
            if held_peice_last_pos != picked_pos:
                selected_tile = 0

            held_piece = 0
            held_peice_last_pos = (0, 0)


    # highlight whichever tile is selected
    if selected_tile != 0:
        g.draw_hex(surface, numpy.add(axial.axial_to_screen(selected_tile, scale), peter_offset), scale, (230, 230, 120))


    # draw whatever the player is holding
    if held_piece != 0 and held_piece.type != NONE:
        g.draw_piece(surface, spritesheet, mousepos, scale, held_piece.type, held_piece.colour)

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