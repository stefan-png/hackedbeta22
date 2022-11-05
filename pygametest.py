import sys, pygame, math
import numpy

import axial

SQRT32 = math.sqrt(3)/2
SQRT3 = math.sqrt(3)
hex_offset = [  
                (-0.5, SQRT32),
                (0.5, SQRT32),
                (1, 0),
                (0.5, -SQRT32),
                (-0.5, -SQRT32),
                (-1, 0),
            ]

light_colour = (216, 189, 138)
mid_colour = (170, 80, 66)
dark_colour = (79, 49, 48)

tile_colours = [light_colour, mid_colour, dark_colour]


screen_width = 800
screen_height = 800
origin = (screen_width/2, screen_height/2)

def draw_hex(pos, scale, colour, width=0):
    
    transformed_offset = []
    for coord in hex_offset:
        # coord * scale + pos
        transformed_offset.append(numpy.add(numpy.array(coord)* scale, pos))

    pygame.draw.polygon(surface, colour, transformed_offset, width)

def draw_board(scale):
    
    yoffset = scale*SQRT3
    half_yoffset = yoffset*0.5
    # draw centreline
    # for y in range(-5, 6):
    #     draw_hex(numpy.add(origin, (0, yoffset*y)), scale,  tile_colours[(y+5)%3])

    # draw sides
    for x in range(6):
        for y in range(-5, 6-x):
            draw_hex(numpy.add(origin, (x*1.5*scale, y*yoffset+half_yoffset*x)), scale,  tile_colours[(x+2*y+5)%3])
            draw_hex(numpy.add(origin, (-x*1.5*scale, y*yoffset+half_yoffset*x)), scale,  tile_colours[(x+2*y+5)%3])

pygame.init()

surface = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont(None, 24)

# game loop
while True:

    # state
    scale = 30

    # draw background
    surface.fill((255, 255, 255, 255))
    draw_board(scale)

    mousepos = pygame.mouse.get_pos()

    axialpos = axial.axial_round(axial.screen_to_axial(numpy.subtract(mousepos, origin), scale))
    pos = numpy.add(axial.axial_to_screen(axialpos, scale), origin)
    draw_hex(pos, scale, (230, 230, 240), 4)
    pygame.draw.circle(surface, (255, 255, 255), pos, scale/3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:            

    
    img = font.render("hovering: " + str(axialpos), True, (1,1,1))
    surface.blit(img, (20, 20))


    # do the transparent stuff maybe 
    pygame.display.flip()