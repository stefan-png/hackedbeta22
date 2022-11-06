import pygame, math, numpy, Peices

light_colour = (216, 189, 138)
mid_colour = (170, 80, 66)
dark_colour = (79, 49, 48)

tile_colours = [light_colour, mid_colour, dark_colour]

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

def get_hex_colour(q, r):
    return tile_colours[(r+2*q+5)%3]

def draw_hex(surface, pos, scale, colour, width=0):
    
    transformed_offset = []
    for coord in hex_offset:
        # coord * scale + pos
        transformed_offset.append(numpy.add(numpy.array(coord)* scale, pos))

    pygame.draw.polygon(surface, colour, transformed_offset, width)

def draw_board(surface, pos, scale):
    
    yoffset = scale*SQRT3
    half_yoffset = yoffset*0.5
    # draw centreline
    # for y in range(-5, 6):
    #     draw_hex(numpy.add(origin, (0, yoffset*y)), scale,  tile_colours[(y+5)%3])

    # draw sides
    for x in range(6):
        for y in range(-5, 6-x):
            draw_hex(surface, numpy.add(pos, (x*1.5*scale, y*yoffset+half_yoffset*x)), scale,  get_hex_colour(x, y))
            draw_hex(surface, numpy.add(pos, (-x*1.5*scale, y*yoffset+half_yoffset*x)), scale,  get_hex_colour(x, y))

def load_spritesheet(filename):
        """Load the sheet."""
        try:
            return pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)

# spritesheet is the sheet to sample from
# rectangle is the image in screen coordinates
# scale is the final scale to draw the image in (width, height)
def image_at(spritesheet, rectangle):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(spritesheet, (0, 0), rect)
        return image

# surface to draw on
# image to draw
# position to draw at
# scale is (width, height)
def draw_image(surface, image, pos, size):
        rect = image.get_rect()
        rect.topleft = pos
        image = pygame.transform.scale(image, size)
        surface.blit(image, rect)

def draw_piece(surface, spritesheet, pos, scale, pieceID, colour):
    kingrect = pygame.Rect(0, 0, 300, 300)
    queenrect = pygame.Rect(300, 0, 300, 300)
    bishrect = pygame.Rect(600, 0, 300, 300)
    horserect = pygame.Rect(900, 0, 300, 300)
    rookrect = pygame.Rect(1200, 0, 300, 300)
    pawnrect = pygame.Rect(1500, 0, 300, 300)
    
    rect = pawnrect

    if pieceID == Peices.KING:
        rect = kingrect
    elif pieceID == Peices.QUEEN:
        rect = queenrect
    elif pieceID == Peices.BISHOP:
        rect = bishrect
    elif pieceID == Peices.KNIGHT:
        rect = horserect
    elif pieceID == Peices.ROOK:
        rect = rookrect

    if colour == Peices.BLACK:
        rect.y += 300

    draw_image(surface, image_at(spritesheet, rect), numpy.subtract(pos, (0.75*scale, 0.80*scale)), (1.5*scale, 1.5*scale))
