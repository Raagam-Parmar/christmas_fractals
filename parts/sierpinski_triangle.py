from manim import *
import numpy as np


def triangle(vertices: list[np.ndarray], stroke_width=DEFAULT_STROKE_WIDTH, stroke_color=BLUE, fill_color=BLUE, fill_opacity=1):
    """
    `triangle v` returns a triangle with vertices being those in the list `v`.
    """
    for i in range(len(vertices)):
        vertices[i] = np.array(vertices[i])

    tri = Polygon(*vertices)
    tri.set_stroke(width=stroke_width, color=stroke_color)
    tri.set_fill(color=fill_color, opacity=fill_opacity)

    return tri


def pattern_helper(vertices: list[np.ndarray], iter: int, fill_color=BLACK, fill_opacity=1):
    """
    `pattern_helper c i` returns the sierpinski triangle without the base triangle, with `i` iterations being made.
    """
    # base case of recursion
    if iter == 0:
        return VGroup()

    # convert all vertices to numpy arrays
    for i in range(len(vertices)):
        vertices[i] = np.array(vertices[i])

    # get all vertices individually
    v_1, v_2, v_3 = vertices[0], vertices[1], vertices[2]

    # get the mid-points of the vertices
    mid_12 = (v_1 + v_2) / 2
    mid_23 = (v_2 + v_3) / 2
    mid_31 = (v_3 + v_1) / 2

    # the new set of vertices, for recursive nature of the triangle
    sub_vertices_1 = [v_1, mid_12, mid_31]
    sub_vertices_2 = [mid_12, v_2, mid_23]
    sub_vertices_3 = [mid_31, mid_23, v_3]

    # the first triangle
    tri = triangle(
        vertices=[ mid_12, mid_23, mid_31 ],
        stroke_width=0,
        fill_color=fill_color,
        fill_opacity=fill_opacity
    )

    # an empty group to hold the sub-pattern
    sub_pattern = VGroup()

    # call the function recursively on the 3 new set of vertices, with one iteration less, and same color options
    sub_pattern.add(
        pattern_helper(sub_vertices_1, iter - 1, fill_color=fill_color, fill_opacity=fill_opacity),
        pattern_helper(sub_vertices_2, iter - 1, fill_color=fill_color, fill_opacity=fill_opacity),
        pattern_helper(sub_vertices_3, iter - 1, fill_color=fill_color, fill_opacity=fill_opacity)
    )

    # return the base triangle, and the sub-pattern as a vectorized-mathematical-object-group
    return VGroup(tri, sub_pattern)


def pattern(vertices: list[np.ndarray], iter: int, fill_color=BLACK, fill_opacity=1, base_color=BLUE):
    """
    `pattern v i` returns the sierpinski triangle with vertices being those in the list `v` and `i` iterations.
    
    `fill_color` is the dominant color of the triangle.
    
    `base_color` is the non-dominant color of the triangle.
    """
    # base triangle
    base_tri = triangle(
        vertices=vertices,
        stroke_width=0,
        fill_color=base_color,
        fill_opacity=fill_opacity,
    )

    # sub-pattern for the fractal
    p = pattern_helper(
        vertices,
        iter,
        fill_color=fill_color,
        fill_opacity=fill_opacity
    )

    return VGroup(base_tri, p)


def pattern_center_width_height(center: list[np.ndarray], width: float, height: float, iter: int, fill_color=BLACK, fill_opacity=1, base_color=BLUE):
    """
    `pattern_center_width_height c w h i` is a modified version of `pattern`.

    returns an upright triangle with base center at `center`, `width` amount wide and `height` amount tall, and `i` iterations    
    """
    left = center - np.array([width / 2, 0, 0])
    right = center + np.array([width / 2, 0, 0])
    top = center + np.array([0, height, 0])

    corners = [left, right, top]

    p = pattern(corners, iter, fill_color, fill_opacity, base_color)
    return p

# trial scene
class Sierpinski(Scene):
    def construct(self):
        self.camera.frame_width = 16
        self.camera.frame_height = 9

        p = pattern(
            vertices= [ 
                [-5, -4, 0],
                [5, -4, 0],
                [0, 4, 0]
            ],
            iter=9,
        )

        p = pattern_center_width_height(
            center=ORIGIN,
            width=2,
            height=1,
            iter=6
        )

        self.add(p)