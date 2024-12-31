from manim import *
import numpy as np

from parts.t_cross_fractal import pattern as t_cross
from parts.sierpinski_triangle import pattern_center_width_height as sierpinski
from parts.snowman_fractal import pattern as snowman_fractal
from parts.vicsek_cross import pattern as vicsek_cross


class Main(Scene):
    def construct(self):
        # sky configuration
        #################################################################################
        # sky is a full-screen rectangle with a gradient of black to gray
        sky = FullScreenRectangle()
        sky.set_stroke(width=0)
        sky.set_fill(opacity=1, color=[BLACK, DARKER_GRAY])
        sky.set_sheen_direction(DOWN)
        #################################################################################



        # ground configuration
        #################################################################################
        # ground_unit is a fourth of the screen width.
        ground_unit = config.frame_width / 4

        # ground_center_coords are the coordinates of the center of the ground
        ground_center_coords = np.array([
            0,
            - (config.frame_height / 2 + ground_unit * 3 / 2),
            0
        ])

        ground = t_cross(ORIGIN, 2 * ground_unit, 9)
        ground.rotate_about_origin(180 * DEGREES)
        ground.move_to(ground_center_coords)

        # set color of the ground as a gradient
        ground.set_color_by_gradient(BLUE_C, WHITE, BLUE_C)

        # ground_level is the y-level of the ground top surface in manim-coordinates.
        ground_level = -config.frame_height / 2 + ground_unit / 2
        #################################################################################


        # mountains configuration
        #################################################################################
        # below are the configurations of the mountains in the backdrop
        mountain_1 = sierpinski(
            center=UP * ground_level,
            width=2,
            height=2,
            iter=7,
            base_color=GRAY_E,
            fill_color=BLACK,
            fill_opacity=1
        )

        mountain_2 = sierpinski(
            center=2.5 * RIGHT + UP * ground_level,
            width=4,
            height=4,
            iter=8,
            base_color=GRAY_E,
            fill_color=BLACK
        )

        mountain_3 = sierpinski(
            center=4 * RIGHT + UP * ground_level,
            width=2,
            height=2,
            iter=7,
            base_color=GRAY_E,
            fill_color=BLACK
        )

        mountain_4 = sierpinski(
            center=8 * RIGHT + UP * ground_level,
            width=8,
            height=8,
            iter=9,
            base_color=GRAY_E,
            fill_color=BLACK
        )

        mountain_5 = sierpinski(
            center=1 * LEFT + UP * ground_level,
            width=1,
            height=1,
            iter=6,
            base_color=GRAY_E,
            fill_color=BLACK
        )

        mountain_6 = sierpinski(
            center=2 * LEFT + UP * ground_level,
            width=2,
            height=2,
            iter=7,
            base_color=GRAY_E,
            fill_color=BLACK
        )

        mountain_7 = sierpinski(
            center=3.5 * LEFT + UP * ground_level,
            width=4,
            height=4,
            iter=8,
            base_color=GRAY_E,
            fill_color=BLACK
        )

        mountain_8 = sierpinski(
            center=8 * LEFT + UP * ground_level,
            width=8,
            height=8,
            iter=9,
            base_color=GRAY_E,
            fill_color=BLACK
        )

        mountains = VGroup(mountain_5, mountain_6, mountain_7, mountain_8, mountain_1, mountain_3, mountain_2, mountain_4)
        #################################################################################



        # snowman configuration
        #################################################################################
        # snowman_x is the x position of the snowman
        snowman_x = -3

        snowman_head_radius = 0.5
        snowman_torso_radius = 1
        snowman_head_center = UP * (snowman_head_radius + 2 * snowman_torso_radius + ground_level) + RIGHT * snowman_x

        # head_angle is the angle at which the snowman looks
        head_angle=15

        # the hat of the snowman
        snowman_hat = snowman_fractal(
            center=snowman_head_center,
            scale=snowman_head_radius,
            color=RED_E,
            theta= 0 * np.pi / 180,
            alpha= 30 * np.pi / 180,
            rho= 0.40,
            iter= 8
        )

        # the head of the snowman, layered on top of the hat
        snowman_head = Circle(radius=snowman_head_radius)
        snowman_head.move_to(snowman_head_center)
        snowman_head.set_stroke(width=0)
        snowman_head.set_fill(color=BLUE_A, opacity=1)

        # the torso of the snowman, below its head
        snowman_torso_center = UP * (snowman_torso_radius + ground_level) + RIGHT * snowman_x
        snowman_torso = Circle(radius=snowman_torso_radius)
        snowman_torso.set_stroke(width=0)
        snowman_torso.set_fill(color=BLUE_A, opacity=1)
        snowman_torso.move_to(snowman_torso_center)

        # the beak of the snowman, as a sierpinski triangle
        snowman_beak_width = 0.35

        # correction is just a large phrase too big to put in a singl variable
        correction = snowman_head_radius - np.sqrt(np.square(snowman_head_radius) - np.square(snowman_beak_width / 2))

        snowman_beak_center = snowman_head_center + RIGHT * snowman_head_radius + LEFT * correction
        snowman_beak = sierpinski(
            center=snowman_beak_center,
            width=snowman_beak_width,
            height=0.75,
            iter=7,
            base_color=WHITE,
            fill_color=ORANGE
        )
        snowman_beak.rotate(- 90 * DEGREES, about_point=snowman_beak_center)

        # create a group of the head and the hat, and rotate it `head_angle` degrees
        head = VGroup(snowman_hat, snowman_head, snowman_beak)
        head.rotate(head_angle * DEGREES, about_point=snowman_head_center)

        snowman = VGroup(head, snowman_torso)
        #################################################################################



        # christmas tree configuration
        #################################################################################
        # ground_tree_dist is the distance of the center of the tree image from the top surface of the ground
        ground_tree_dist = - ground_level + 0.9 * UP

        christmas_tree_x = 3.5
        christmas_tree_scale = 0.165
        christmas_tree_center = UP * ground_tree_dist * christmas_tree_scale / 0.2 + UP * ground_level + RIGHT * christmas_tree_x
        christmas_tree = ImageMobject('./images/tree.png')
        christmas_tree.scale(christmas_tree_scale)
        christmas_tree.move_to(christmas_tree_center)
        #################################################################################




        # side trees configuration
        #################################################################################
        # below are the configurations of the left tand right trees to the main christmas tree
        tree_1_x = 1.75
        tree_1_scale = 0.1
        tree_1_center = UP * ground_tree_dist * tree_1_scale / 0.2 + UP * ground_level + RIGHT * tree_1_x
        tree_1 = ImageMobject('./images/tree.png')
        tree_1.scale(tree_1_scale)
        tree_1.move_to(tree_1_center)

        tree_2_x = 5
        tree_2_scale = 0.135
        tree_2_center = UP * ground_tree_dist * tree_2_scale / 0.2 + UP * ground_level + RIGHT * tree_2_x
        tree_2 = ImageMobject('./images/tree.png')
        tree_2.scale(tree_2_scale)
        tree_2.move_to(tree_2_center)
        #################################################################################




        # golden star configuration
        #################################################################################
        golden_star_scale = 0.01
        golden_star_center = christmas_tree_center + UP * 5.1 + UP * ground_level
        golden_star = ImageMobject('./images/golden_star.png')
        golden_star.scale(golden_star_scale)
        golden_star.move_to(golden_star_center)
        #################################################################################




        # snow flakes configuration
        #################################################################################
        n_flakes = 50

        flakes = VGroup()

        for _ in range(n_flakes):
            # a set of colors to choose from WHITE being prioritised more
            flake_colors_choices = [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E, WHITE, WHITE, WHITE]

            # a set of randomly chosen colors form the above list
            random_colors = [ np.random.choice(flake_colors_choices) for _ in range(3) ]

            # random cener of the flake
            flake_center_x = np.random.uniform(-7.5, 7.5)
            flake_center_y = np.random.uniform(ground_level, 4)
            flake_center = np.array([flake_center_x, flake_center_y, 0])

            # random orientation of the flake
            flake_orient = np.random.uniform(0, 90) * DEGREES

            # random scale of the flake
            flake_scale = np.random.uniform(0.7, 2) / 32

            # rawing the flake
            flake = vicsek_cross(flake_center, flake_scale, 4)
            flake.set_stroke(width=0)
            flake.set_fill(opacity=1, color=random_colors )
            flake.rotate(flake_orient, about_point=flake_center)

            flakes.add(flake)
        #################################################################################

        # layering the different objects in the scene
        self.add(sky, mountains, tree_1, tree_2, snowman, christmas_tree, golden_star, ground, flakes)
