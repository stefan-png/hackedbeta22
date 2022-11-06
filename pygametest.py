import sys, pygame, math
import numpy

import axial, graphics as g

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
    scale = 40

    # draw background
    surface.fill((255, 255, 255, 255))
    g.draw_board(surface, origin, scale)

    mousepos = pygame.mouse.get_pos()

    axialpos = axial.axial_round(axial.screen_to_axial(numpy.subtract(mousepos, origin), scale))
    pos = numpy.add(axial.axial_to_screen(axialpos, scale), origin)
    g.draw_hex(surface, pos, scale, (230, 230, 240), 4)
    pygame.draw.circle(surface, (255, 255, 255), pos, scale/3)
    g.draw_piece(surface, spritesheet, pos, scale, "knight", "white")
    g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((1, 0), scale), origin), scale, "queen", "white")
    g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((2, 0), scale), origin), scale, "rook", "white")
    g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((1, 1), scale), origin), scale, "bishop", "black")
    g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((2, 1), scale), origin), scale, "king", "black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:            

    
    img = font.render("hovering: " + str(axialpos), True, (1,1,1))
    surface.blit(img, (20, 20))


    # do the transparent stuff maybe 
    pygame.display.flip()