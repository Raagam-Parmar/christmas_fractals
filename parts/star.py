# Credits for the code to:
# https://stackoverflow.com/questions/71786983/chaos-game-fractal-not-rendering-correctly

import pygame
import os
import random
import math

# degrees to radians conversion
DEGREES = math.pi / 180

# some constant colors
GOLDEN_YELLOW = (255, 223, 0)

# image dimensions
WIDTH  = 9_000
HEIGHT = 9_000

# initialize pygame
pygame.init()

# transparent surface with required dimensions
background = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
background.fill((0, 0, 0, 0))


def pattern(surface: pygame.surface, points: int, color: list[int]):
    """
    `pattern s p c` makes the star pattern on the surface `s`, containing `p` many points of color `c`.
    """
    # offset of vertices of the star from the border, 
    # 1 for edge-to-edge image
    border = 1

    # vertices of the star, as a pentagon
    A = (WIDTH / 2, border)
    B = (WIDTH - border, HEIGHT * 0.5 * math.tan(36 * DEGREES))
    C = (WIDTH * math.cos(36 * DEGREES), HEIGHT - border)
    D = (WIDTH * (1 - math.cos(36 * DEGREES)), HEIGHT - border)
    E = (border, HEIGHT * 0.5 * math.tan(36 * DEGREES))

    vertices = [A, B, C, D, E]

    # indices of last and last-second vertices
    last_vertex = 0
    second_last_vertex = 0

    # a random starting point, the center of the canvas
    p = (int(WIDTH / 2), int(HEIGHT / 2))
    
    for _ in range(points):
        # choose a random vertex
        v = random.randint(0, 4)

        # if the previous two vertices were the same, and the current selected vertex is 1 or 4 places away from the previous vertex,
        # select a new vertex
        if last_vertex == second_last_vertex:
            while (v == (last_vertex - 1) % 5) or (v == (last_vertex + 1) % 5):
                v = v = random.randint(0, 4)

        # cycle the vertices
        second_last_vertex = last_vertex
        last_vertex = v

        # update random point to the newly chosen point
        p_x = ( vertices[v][0] + p[0] ) / 2
        p_y = ( vertices[v][1] + p[1] ) / 2
        p = (int(p_x), int(p_y))

        # set surface color at the point
        surface.set_at(p, color)

# draw the star in golden-yellow color
pattern(
    surface=background,
    points=10_000_000,
    color=GOLDEN_YELLOW
)

# save the star as a transparent image
os.makedirs('images/')
output_path = os.path.join(os.getcwd(), 'images/golden_star.png')
pygame.image.save(background, output_path)

print(f"Golden star PNG saved at: {output_path}")

# quit pygame
pygame.quit()
