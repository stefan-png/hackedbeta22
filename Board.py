import numpy as np
from Peices import *
import sys, pygame, math
import axial, graphics as g
import Evaluation as Eval
from pygametest import *

def set_Up_Board(mode=0, Winner=None): # creates board and peices for the starting position of the game
    #creates the a hexagonal 2 dimensional grid o fhte board
    output = np.ones(shape=(20, 20), dtype=object)
    for q in range(0, 11):
        for r in range(0, 11):
            if q + r >= 5 and q + r <= 15:
                output[q, r] = 0

    if mode== 2:
        ref = 2
        return output

    if mode == 0: #glinski's set up of the board
        # white bishops
        output[10,5] = peices(BISHOP, WHITE)
        output[9,5] = peices(BISHOP, WHITE)
        output[8,5] = peices(BISHOP, WHITE)
        #white queen
        output[10,4] = peices(QUEEN, WHITE)
        #white king
        output[9,6] = peices(KING, WHITE)
        #white knights
        output[10, 3] = peices(KNIGHT, WHITE)
        output[8,7] = peices(KNIGHT, WHITE)
        #white rooks
        output[10,2] = peices(ROOK, WHITE)
        output[7,8] = peices(ROOK, WHITE)
        # white pawns
        output[10, 1] = peices(PAWN, WHITE)
        output[9, 2] = peices(PAWN, WHITE)
        output[8, 3] = peices(PAWN, WHITE)
        output[7, 4] = peices(PAWN, WHITE)
        output[6, 5] = peices(PAWN, WHITE)
        output[6, 6] = peices(PAWN, WHITE)
        output[6, 7] = peices(PAWN, WHITE)
        output[6, 8] = peices(PAWN, WHITE)
        output[6, 9] = peices(PAWN, WHITE)
        # black bishops
        output[0, 5] = peices(BISHOP, BLACK)
        output[1, 5] = peices(BISHOP, BLACK)
        output[2, 5] = peices(BISHOP, BLACK)
        # black queen
        output[1, 4] = peices(QUEEN, BLACK)
        # black king
        output[0, 6] = peices(KING, BLACK)
        # black knights
        output[2, 3] = peices(KNIGHT, BLACK)
        output[0, 7] = peices(KNIGHT, BLACK)
        # black rooks
        output[3, 2] = peices(ROOK, BLACK)
        output[0, 8] = peices(ROOK, BLACK)
        #black pawns
        output[4, 1] = peices(PAWN, BLACK)
        output[4, 2] = peices(PAWN, BLACK)
        output[4, 3] = peices(PAWN, BLACK)
        output[4, 4] = peices(PAWN, BLACK)
        output[4, 5] = peices(PAWN, BLACK)
        output[3, 6] = peices(PAWN, BLACK)
        output[2, 7] = peices(PAWN, BLACK)
        output[1, 8] = peices(PAWN, BLACK)
        output[0, 9] = peices(PAWN, BLACK)
    if mode == 1:
        output[4,0] = peices(PAWN, BLACK)
        output[3, 1] = peices(ROOK, BLACK)
        output[2, 2] = peices(KNIGHT, BLACK)
        output[1, 3] = peices(BISHOP, BLACK)
        output[0,4] = peices(QUEEN, BLACK)
        output[0,5] = peices(KING, BLACK)
        output[6, 10] = peices(PAWN, WHITE)
        output[7, 9] = peices(ROOK, WHITE)
        output[8, 8] = peices(KNIGHT, WHITE)
        output[9, 7] = peices(BISHOP, WHITE)
        output[10, 6] = peices(QUEEN, WHITE)
        output[10, 5] = peices(KING, WHITE)
        return grid_Maker(output)
    if mode == 3:
        for q in range(0, 11):
            for r in range(0, 11):
                if q + r >= 5 and q + r <= 15:
                    output[q,r] = output[10, 5] = peices(KING, Winner)

    return output

def grid_Maker(output): # creates mock game to set up board then returns board
    screen_width = 800
    screen_height = 800
    origin = (screen_width/2, screen_height/2)

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF, 32)
    surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA, 32)

    spritesheet = g.load_spritesheet("chesspieces.png")
    font = pygame.font.SysFont(None, 24)

# setup board
    grid = output
    selected_tile = NONE

    while True:
        # state
        scale = 35

        # draw background
        surface.fill((255, 255, 255, 255))
        g.draw_board(surface, origin, scale)

        mousepos = pygame.mouse.get_pos()

        peter_offset = ((screen_width - 15 * scale) / 2, (screen_height - 15 * math.sqrt(3) * scale) / 2)

        picked_pos = axial.axial_round(axial.screen_to_axial(np.subtract(mousepos, peter_offset), scale))
        pos = np.add(axial.axial_to_screen(picked_pos, scale), peter_offset)
        g.draw_hex(surface, pos, scale, (230, 230, 240), 4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # before quiting, returns grid without the peices outside of the board
                for q in range(0, 11):
                    for r in range(0, 11):
                        if (q + r < 5 or q + r > 15):
                            grid[q,r] = 1
                return grid
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not Eval.check_on_board(flipxy(picked_pos)) and grid[flipxy(picked_pos)] in [0, 1]:
                    # we have selected a tile outside board that dosnt have a peice
                    selected_tile = 0
                elif selected_tile == 0 or grid[flipxy(selected_tile)] == 0:
                    # we havent selected a tile yet, select one
                    selected_tile = picked_pos
                elif picked_pos == selected_tile:
                    # we picked the same as is selected
                    selected_tile = 0
                elif not Eval.check_on_board(flipxy(selected_tile)):
                    # we have selected a tile outside the board that does have a peice
                    print(selected_tile)
                    grid[picked_pos[1], picked_pos[0]] = grid[selected_tile[1], selected_tile[0]]
                    selected_tile = 0
                else:
                    # on the board, no change
                    grid[picked_pos[1], picked_pos[0]] = grid[selected_tile[1], selected_tile[0]]
                    grid[selected_tile[1], selected_tile[0]] = 0
                    selected_tile = 0

        if selected_tile != 0:
            g.draw_hex(surface, numpy.add(axial.axial_to_screen(selected_tile, scale), peter_offset), scale,
                       (230, 230, 120))

        if selected_tile != 0 and grid[selected_tile[1], selected_tile[0]] not in [0, 1]:
            for move in Eval.possible_moves(grid, (selected_tile[1], selected_tile[0])):
                pygame.draw.circle(surface, g.get_hex_colour(move[1], move[0] + 2),
                                   numpy.add(axial.axial_to_screen((move[1], move[0]), scale), peter_offset),
                                   scale * g.SQRT32 / 2)

        img = font.render("hovering: " + str(picked_pos), True, (1, 1, 1))
        surface.blit(img, (20, 20))

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[x, y] in [0, 1]:
                    continue
                piece = grid[x, y].type
                colour = grid[x, y].colour
                g.draw_piece(surface, spritesheet, numpy.add(axial.axial_to_screen((y, x), scale), peter_offset),
                             scale, piece, colour)
        screen.blit(surface, (0, 0))
        pygame.display.flip()