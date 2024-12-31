from manim import *
import numpy as np

# custom directions
up = 2 * UP
down = 2 * DOWN
left = 2 * LEFT
right = 2 * RIGHT

# the sides of an ith iteration vicsek fractal can be broken down into 
# the sides of (i-1)th iteration vicsek fractal
# below are the definitions of the four sides in terms of the previous iteration fractal
def bottom_left(center: np.ndarray, scale: float, iter: int):
    # base case
    if iter == 0:
        part = [
            [-1, -3, 0],
            [-1, -1, 0],
            [-3, -1, 0]
        ]

        for i in range(len(part)):
            part[i] = np.array(part[i])
            part[i] = np.array(center) + (scale * part[i])

        return part
    
    # recursion case
    center_down = np.array(center) + (scale * down)
    center_left = np.array(center) + (scale * left)

    part = \
        bottom_left(center_down, scale / 3, iter - 1) + \
        top_left(center_down, scale / 3, iter - 1) + \
        bottom_left(center, scale / 3, iter - 1) + \
        bottom_right(center_left, scale / 3, iter - 1) + \
        bottom_left(center_left, scale / 3, iter - 1)
    
    return part
    
def top_left(center: np.ndarray, scale: float, iter: int):
    # base casr
    if iter == 0:
        part = [
            [-3, 1, 0],
            [-1, 1, 0],
            [-1, 3, 0]
        ]

        for i in range(len(part)):
            part[i] = np.array(part[i])
            part[i] = np.array(center) + (scale * part[i])

        return part
    
    # recursion case
    center_left = np.array(center) + (scale * left)
    center_up = np.array(center) + (scale * up)

    part = \
        top_left(center_left, scale / 3, iter - 1) + \
        top_right(center_left, scale / 3, iter - 1) + \
        top_left(center, scale / 3, iter - 1) + \
        bottom_left(center_up, scale / 3, iter - 1) + \
        top_left(center_up, scale / 3, iter - 1)
    
    return part

def top_right(center: np.ndarray, scale: float, iter: int):
    # base case
    if iter == 0:
        part = [
            [1, 3, 0],
            [1, 1, 0],
            [3, 1, 0]
        ]

        for i in range(len(part)):
            part[i] = np.array(part[i])
            part[i] = np.array(center) + (scale * part[i])

        return part
    
    # recursion case
    center_up = np.array(center) + (scale * up)
    center_right = np.array(center) + (scale * right)

    part = \
        top_right(center_up, scale / 3, iter - 1) + \
        bottom_right(center_up, scale / 3, iter - 1) + \
        top_right(center, scale / 3, iter - 1) + \
        top_left(center_right, scale / 3, iter - 1) + \
        top_right(center_right, scale / 3, iter - 1)
    
    return part
    
def bottom_right(center: np.ndarray, scale: float, iter: int):
    # base case
    if iter == 0:
        part = [
            [3, -1, 0],
            [1, -1, 0],
            [1, -3, 0]
        ]

        for i in range(len(part)):
            part[i] = np.array(part[i])
            part[i] = np.array(center) + (scale * part[i])

        return part
    
    # recursion case
    center_right = np.array(center) + (scale * right)
    center_down = np.array(center) + (scale * down)

    part = \
        bottom_right(center_right, scale / 3, iter - 1) + \
        bottom_left(center_right, scale / 3, iter - 1) + \
        bottom_right(center, scale / 3, iter - 1) + \
        top_right(center_down, scale / 3, iter - 1) + \
        bottom_right(center_down, scale / 3, iter - 1)
    
    return part

def pattern(center: np.ndarray, scale: float, iter: int):
    """
    `pattern c s i` returns the vicsek corss fractal as a polygon, with center at `c`, scale of `s`, of i-iterations.
    """
    corners = \
        bottom_left(center, scale, iter) + \
        top_left(center, scale, iter) + \
        top_right(center, scale, iter) + \
        bottom_right(center, scale, iter)
    
    return Polygon(*corners)

# trial scene
class Vicsek_Cross(Scene):
    def construct(self):
        iterations = 5
        p = []

        for i in range(iterations + 1):
            pi = pattern(ORIGIN, 1, i)
            pi.set_stroke(width=0)
            pi.set_fill(BLUE, opacity=1)

            p += pi

        self.play(Create(p[0]), run_time=3)

        for i in range(iterations):
            self.play(Transform(p[i], p[i + 1]))
            self.add(p[i + 1])
            self.remove(p[i])

        self.wait(1)
        self.play(FadeOut(p[iterations]), run_time=1.5)
        self.wait(1)