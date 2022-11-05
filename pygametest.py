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

def draw_hex(pos, scale, colour):
    
    transformed_offset = []
    for coord in hex_offset:
        # coord * scale + pos
        transformed_offset.append(numpy.add(numpy.array(coord)* scale, pos))

    pygame.draw.polygon(surface, colour, transformed_offset)

def draw_board(scale):
    
    yoffset = scale*SQRT3
    half_yoffset = yoffset*0.5
    origin = (400, 400)
    # draw centreline
    # for y in range(-5, 6):
    #     draw_hex(numpy.add(origin, (0, yoffset*y)), scale,  tile_colours[(y+5)%3])

    # draw sides
    for x in range(6):
        for y in range(-5, 6-x):
            draw_hex(numpy.add(origin, (x*1.5*scale, y*yoffset+half_yoffset*x)), scale,  tile_colours[(x+2*y+5)%3])
            draw_hex(numpy.add(origin, (-x*1.5*scale, y*yoffset+half_yoffset*x)), scale,  tile_colours[(x+2*y+5)%3])

pygame.init()

surface = pygame.display.set_mode((800, 800))


# game loop
while True:

    # state
    scale = 30

    # draw background
    surface.fill((255, 255, 255))
    draw_board(scale)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
            

    mousepos = pygame.mouse.get_pos()
    pos = numpy.floor(numpy.array(axial.screen_to_axial(mousepos, scale))/scale)*scale
    draw_hex(axial.axial_to_screen(pos, scale), scale, (20, 230, 40))

    pygame.display.flip()