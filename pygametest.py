import sys, pygame, math

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

def draw_hex(pos, scale, colour):
    
    transformed_offset = []
    for coord in hex_offset:
        transformed_offset.append((coord[0]*scale+pos[0], coord[1]*scale+pos[1]))

    pygame.draw.polygon(surface, colour, transformed_offset)

pygame.init()

surface = pygame.display.set_mode((800, 800))


light_colour = (216, 189, 138)
mid_colour = (170, 80, 66)
dark_colour = (79, 49, 48)


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    scale = 100
    half_yoffset = scale*SQRT32
    yoffset = scale*SQRT3

    draw_hex((100, scale), scale,  light_colour)
    draw_hex((100, scale+1*yoffset), scale,  mid_colour)
    draw_hex((100, scale+2*yoffset), scale,  dark_colour)

    draw_hex((100+3/2*scale, scale+half_yoffset), scale,  dark_colour)
    draw_hex((100+3/2*scale, scale+3*half_yoffset), scale,  light_colour)
    draw_hex((100+3/2*scale, scale+5*half_yoffset), scale,  mid_colour)

    draw_hex((100+3*scale, scale), scale,  light_colour)
    draw_hex((100+3*scale, scale+1*yoffset), scale,  mid_colour)
    draw_hex((100+3*scale, scale+2*yoffset), scale, dark_colour)

    pygame.display.flip()