from manim import *
import math

class Basis(Scene):
    def construct(self):
        data_points = [(0.2, 0.1),
                       (0.3, 0.2), 
                       (0.5, 0.4),
                       (0.7, 0.2),
                       (0.1, 0.3),
                       (1, 0.23),
                       (1.2, 0.43),
                       (1.4, 0.2),
                       (1.7, 0.1),
                       (1.8, 0.23),
                       (2.3, 0.23),
                       (2.7, 0.12),
                       (2.8, 0.23), 
                       (3.1, 0.35), 
                       (3.2, 0.12), 
                       (3.4, 0.23),

                       (0.12, 0.15),
                       (0.14, 0.16),
                       (0.21, 0.24),
                       (0.24, 0.26),
                       (0.25, 0.29),
                       (0.31, 0.3),
                       (0.34, 0.31),
                       (0.44, 0.47),
                       (0.7, 0.79),
                       (1.11, 1.02),
                       (1.23, 1.32),
                       (1.35, 1.41),
                       (1.65, 1.7),
                       (1.82, 1.78),
                       (2.11, 2.10),
                       (2.34, 2.47),
                       (2.5, 2.5),
                       
                       (0.1, 0.1), 
                       (0.3, 0.2),
                       (0.22, 0.45),
                       (0.34, 0.72),
                       (0.24, 1.02),
                       (0.32, 1.23),
                       (0.21, 1.25),
                       (0.3, 1.45),
                       (0.12, 1.6),
                       (0.3, 1.77),
                       (0.21, 2.1),
                       (0.31, 2.32),
                       (0.25, 2.4),
                       (0.26, 2.63),
                       (0.12, 2.8),
                       (0.3, 3.1)]
        
        ax = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=6, y_length=6)
        ax_2 = ax.copy()
                       
        dots = VGroup()
        for x, y in data_points:
            dot = Dot(ax.c2p(x, y, 0), color=BLUE_E)  # Convert data point to scene coordinates
            dots.add(dot)

        axes_group = VGroup(ax, dots)
        axes_group_2 = VGroup(ax_2, dots.copy())

        axes_group.scale(0.75)
        axes_group.shift(LEFT*3 + UP*0.5)
        complete_label = Text("Complete Basis").scale(0.6)
        complete_label.next_to(axes_group, DOWN, buff=0.2)
        axes_group.add(complete_label)

        axes_group_2.scale(0.75)
        axes_group_2.shift(RIGHT*3 + UP*0.5)
        overcomplete_label = Text("Overcomplete Basis").scale(0.6)
        overcomplete_label.next_to(axes_group_2, DOWN, buff=0.2)
        axes_group_2.add(overcomplete_label)

        axes_1_origin = ax.c2p(0, 0, 0)
        axes_2_origin = ax_2.c2p(0, 0, 0)
        OC_diag = math.sqrt(1/2)

        basis_vector_x = Arrow(axes_1_origin, ax.c2p(1, 0, 0), color=BLUE, buff=0)
        basis_vector_y = Arrow(axes_1_origin, ax.c2p(0, 1, 0), color=RED, buff=0)

        basis_vector_x_OC = Arrow(axes_2_origin, ax_2.c2p(1, 0, 0), color=BLUE, buff=0)
        basis_vector_y_OC = Arrow(axes_2_origin, ax_2.c2p(0, 1, 0), color=RED, buff=0)
        basis_vector_OC = Arrow(axes_2_origin, ax_2.c2p(OC_diag, OC_diag, 0), color=YELLOW, buff=0)

        axes_group.add(basis_vector_x, basis_vector_y)
        axes_group_2.add(basis_vector_x_OC, basis_vector_y_OC, basis_vector_OC)

        self.play(FadeIn(axes_group, axes_group_2))
        self.wait()

        self.play(basis_vector_y.animate.put_start_and_end_on(axes_1_origin, ax.c2p(0, 2.5, 0)), 
                  basis_vector_x.animate.put_start_and_end_on(ax.c2p(0, 2.5, 0), ax.c2p(2.5, 2.5, 0)),

                  basis_vector_y_OC.animate.put_start_and_end_on(ax_2.c2p(1.25, 1.25, 0), ax_2.c2p(1.25, 2.5, 0)),
                  basis_vector_x_OC.animate.put_start_and_end_on(ax_2.c2p(1.25, 2.5, 0), ax_2.c2p(2.5, 2.5, 0)),
                  basis_vector_OC.animate.put_start_and_end_on(axes_2_origin, ax_2.c2p(1.25, 1.25, 0)))



        