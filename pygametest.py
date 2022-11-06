import sys, pygame, math
import numpy

import axial, graphics as g, Board

screen_width = 800
screen_height = 800
origin = (screen_width/2, screen_height/2)

pygame.init()
surface = pygame.display.set_mode((screen_width, screen_height))

spritesheet = g.load_spritesheet("chesspieces.png")
font = pygame.font.SysFont(None, 24)
    
# game loop
while True:

    # state
    scale = 20

    # draw background
    surface.fill((255, 255, 255, 255))
    g.draw_board(surface, origin, scale)

    mousepos = pygame.mouse.get_pos()

    peter_offset = ( (screen_width-15*scale)/2, (screen_height-15*math.sqrt(3)*scale)/2 )

    axialpos = axial.axial_round(axial.screen_to_axial(numpy.subtract(mousepos, peter_offset), scale))
    pos = numpy.add(axial.axial_to_screen(axialpos, scale), peter_offset)
    g.draw_hex(surface, pos, scale, (230, 230, 240), 4)
    pygame.draw.circle(surface, (255, 255, 255), pos, scale/3)
    g.draw_piece(surface, spritesheet, pos, scale, "knight", "white")
    g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((1, 0), scale), peter_offset), scale, Board.QUEEN, Board.WHITE)
    g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((2, 0), scale), peter_offset), scale, Board.ROOK, Board.WHITE)
    g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((1, 1), scale), peter_offset), scale, Board.BISHOP, Board.WHITE)
    g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((2, 1), scale), peter_offset), scale, Board.KING, Board.WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:            

    
    img = font.render("hovering: " + str(axialpos), True, (1,1,1))
    surface.blit(img, (20, 20))

    # draw setup board
    grid = Board.set_Up_Board()

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[x,y] in [0, 1]:
                continue
            piece = grid[x, y].type
            colour = grid[x, y].colour
            g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((x, y), scale), peter_offset), scale, piece, colour)


    # do the transparent stuff maybe 
    pygame.display.flip()