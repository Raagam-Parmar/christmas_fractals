from manim import *
import numpy as np

def rotate(vector: np.ndarray, radians: float):
    """
    `rotate v r` rotates the vector `v` by `r` radians and returns it.
    """

    # rotation matrix
    rotation_matrix = np.array([
        [np.cos(radians), -np.sin(radians), 0],
        [np.sin(radians), np.cos(radians), 0],
        [0, 0, 1]
    ])

    # return the rotated vector
    return rotation_matrix @ vector


def pattern(center: np.ndarray, scale: float, color: ParsableManimColor, theta: float, alpha: float, rho: float, iter: int):
    """
    `pattern center scale color theta alpha rho iter` returns a `VGroup` 
    of the snowman fractal.
    
    `center` is the center of base-circle.

    `scale` is the radius of base-circle.
    
    `color` is the color of the entire fractal.

    `theta` is the offset of the fractal arms from the `UP` direction in radians.

    `alpha` is the angular distance between the arms of the fractal in radians.

    `rho` is the ratio between the current and next circle in the fractal.

    `iter` is the number of iterations to perform. 
    """
    # base case of recursion
    if iter == 0:
        return VGroup()
    
    # the circle
    circle = Circle(radius=scale)
    circle.move_to(center)
    circle.set_stroke(width=0)
    circle.set_fill(color=color, opacity=1)

    # direction vector along `theta`
    base_dir = rotate(UP, theta) * scale

    # recursive directin vectors `alpha` and `-alpha` away from the base direction
    dir_1 = rotate(base_dir, alpha) * (1 + rho)
    dir_2 = rotate(base_dir, -alpha) * (1 + rho)

    # the first arm
    p1 = pattern(
        center= dir_1 + center, 
        scale= scale * rho,
        color= color,
        theta= theta + alpha,
        alpha= alpha,
        rho= rho,
        iter= iter - 1
    )

    # the second arm
    p2 = pattern(
        center= dir_2 + center, 
        scale= scale * rho,
        color= color,
        theta= theta - alpha,
        alpha= alpha,
        rho= rho,
        iter= iter - 1
    )

    # return the entire structure as a group
    return VGroup(circle, p1, p2)

# trial scene
class Snowman(Scene):
    def construct(self):
        p1 = pattern(
            center= DOWN,
            scale= 2,
            color= RED,
            theta= 0 * DEGREES,
            alpha= 30 * DEGREES,
            rho= 0.40,
            iter= 5
        )

        self.add(p1)