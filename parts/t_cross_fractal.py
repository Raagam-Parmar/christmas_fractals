from manim import *
import numpy as np

def pattern_helper(center: np.ndarray, scale: float, iter: int):
    """
    `pattern_helper c s i` returns the i-th iteration-fractal without the base-square, at center `c`, with scale `s`.
    """
    # recursion base case
    if iter == 0:
        return VGroup()
    
    # the square
    square = Square(scale)
    square.move_to(center)
    square.set_fill(color=BLACK, opacity=1)
    square.set_stroke(width=0)

    # centers of the next squares
    next_1 = scale / 2 * UR + center
    next_2 = scale / 2 * DR + center
    next_3 = scale / 2 * DL + center
    next_4 = scale / 2 * UL + center

    # calling function recursively for the fractal pattern
    s_1 = pattern_helper(next_1, scale / 2, iter - 1)
    s_2 = pattern_helper(next_2, scale / 2, iter - 1)
    s_3 = pattern_helper(next_3, scale / 2, iter - 1)
    s_4 = pattern_helper(next_4, scale / 2, iter - 1)

    return VGroup(square, s_1, s_2, s_3, s_4)

def pattern(center: np.ndarray, scale: float, iter: int):
    """
    `pattern c s i` returns the i-th iteration, t-cross fractal, centered at `c`, and of scale `s`.
    """
    # the base square
    base = Square(2 * scale)
    base.move_to(center)
    base.set_fill(color=BLUE, opacity=1)
    base.set_stroke(width=0)

    return VGroup(base, pattern_helper(center, scale, iter))

# trial scene
class TCross(Scene):
    def construct(self):
        p = pattern(6 * DOWN, 4, 6)
        self.add(p.set_color_by_gradient(BLUE_E, WHITE, BLUE_A))
