from manim import *

PHI_OG = 0*DEGREES
THETA_OG = -90*DEGREES
GAMMA_OG = 0*DEGREES
PHI_CONV = -75*DEGREES
THETA_CONV = 0*DEGREES
GAMMA_CONV = 90*DEGREES

class Relu(ThreeDScene):
    def construct(self):
        feature_map_R = Square(side_length=2.5, fill_opacity=0.9, color=RED)   
        feature_map_R_label = Text("feature map R 2").scale(0.5)
        feature_map_G = Square(side_length=2.5, fill_opacity=0.75, color=GREEN)
        feature_map_G.shift(IN*0.2)
        feature_map_G_label = Text("feature map G 2").scale(0.5)
        feature_map_B = Square(side_length=2.5, fill_opacity=0.6, color=BLUE)
        feature_map_B.shift(IN*0.4)
        feature_map_B_label = Text("feature map B 2").scale(0.5)

        feature_map_B.next_to(feature_map_G, LEFT, buff=0.1)
        feature_map_R.next_to(feature_map_G, RIGHT, buff=0.1)

        feature_map_R_label.move_to(feature_map_R)
        feature_map_G_label.move_to(feature_map_G)
        feature_map_B_label.move_to(feature_map_B)

        feature_map_group = VGroup(feature_map_B, feature_map_B_label, 
                                   feature_map_G, feature_map_G_label,
                                   feature_map_R, feature_map_R_label)

        self.add(feature_map_group)
        self.wait()
        self.play(feature_map_B_label.animate.move_to(feature_map_G),
                  feature_map_R_label.animate.move_to(feature_map_G),
                  feature_map_B.animate.move_to(feature_map_G),
                  feature_map_R.animate.move_to(feature_map_G))
        self.wait()
        self.play(feature_map_group.animate.shift(LEFT*3))

        ax = Axes(x_range=[-5, 5, 1], y_range=[0, 5, 1], x_length=10, y_length=5)
        
        line = Line(ax.c2p(-5, 0, 0), ax.c2p(0, 0, 0), color=RED, stroke_width=4)
        line_2 = Arrow(ax.c2p(0, 0, 0), ax.c2p(5, 5, 0), color=RED, stroke_width=4, buff=0)

        relu = VGroup(ax, line, line_2).scale(0.4)
        relu.shift(RIGHT*3)

        relu_label = Text("ReLU").scale(0.6)
        relu_label.next_to(relu, DOWN, buff=0.2)
        relu.add(relu_label)

        arrow = Arrow().scale(0.6)

        self.play(FadeIn(relu))
        self.play(Create(arrow))
        self.wait()

        self.play(FadeOut(relu, arrow), feature_map_group.animate.shift(RIGHT*3))

        input_R = Square(side_length=4, color=RED, fill_opacity=0.9)
        input_R_label = Text("HR Patch R").scale(0.6)
        input_R_label.move_to(input_R)
        input_G = Square(side_length=4, color=GREEN, fill_opacity=0.75)
        input_G_label = Text("HR Patch G").scale(0.6)
        input_G_label.move_to(input_G)
        input_B = Square(side_length=4, color=BLUE, fill_opacity=0.6)
        input_B_label = Text("HR Patch B").scale(0.6)
        input_B_label.move_to(input_B)

        rgb_group = VGroup(input_B, input_B_label, input_G, input_G_label, input_R, input_R_label)
        
        self.play(Transform(feature_map_group, rgb_group))
        #self.play(feature_map_group.animate.scale(1.6))
        self.move_camera(phi=PHI_CONV, theta=THETA_CONV, gamma=GAMMA_CONV)
        self.play(feature_map_group.animate.shift(IN*4))
        self.play(feature_map_G.animate.shift(IN*0.2), feature_map_B.animate.shift(IN*0.4))
        self.wait()

class ConvNet(ThreeDScene):
    def construct(self):
        #orientation lock
        PHI_OG = 0*DEGREES
        THETA_OG = -90*DEGREES
        GAMMA_OG = 0*DEGREES
        PHI_CONV = -75*DEGREES
        THETA_CONV = 0*DEGREES
        GAMMA_CONV = 90*DEGREES

        input_R = Square(side_length=4, color=RED, fill_opacity=0.9)
        input_R_label = Text("HR Patch R").scale(0.6)
        input_R_label.move_to(input_R)
        input_G = Square(side_length=4, color=GREEN, fill_opacity=0.75)
        input_G_label = Text("HR Patch G").scale(0.6)
        input_G_label.move_to(input_G)
        input_B = Square(side_length=4, color=BLUE, fill_opacity=0.6)
        input_B_label = Text("HR Patch B").scale(0.6)
        input_B_label.move_to(input_B)

        rgb_group = VGroup(input_B, input_B_label, input_G, input_G_label, input_R, input_R_label)
        rgb_group.shift(IN*4)

        feature_map_R = Square(side_length=2.5, fill_opacity=0.9, color=RED)   
        feature_map_R_label = Text("HR Patch R").scale(0.6)
        feature_map_G = Square(side_length=2.5, fill_opacity=0.75, color=GREEN)
        feature_map_G.shift(IN*0.2)
        feature_map_G_label = Text("HR Patch G").scale(0.6)
        feature_map_B = Square(side_length=2.5, fill_opacity=0.6, color=BLUE)
        feature_map_B.shift(IN*0.4)
        feature_map_B_label = Text("HR Patch B").scale(0.6)

        feature_map_group = VGroup(feature_map_B, feature_map_G, feature_map_R)

        output_R = Square(side_length=1/5, fill_opacity=0, stroke_opacity=0.9, color=WHITE) 
        output_R.next_to(feature_map_R, UP + LEFT, buff=-1/5)  
        output_G = Square(side_length=1/5, fill_opacity=0, stroke_opacity=0.75, color=WHITE)   
        output_G.next_to(feature_map_G, UP + LEFT, buff=-1/5)
        output_B = Square(side_length=1/5, fill_opacity=0, stroke_opacity=0.6, color=WHITE)   
        output_B.next_to(feature_map_B, UP + LEFT, buff=-1/5)

        output_R_vertices = output_R.get_vertices()
        output_B_vertices = output_B.get_vertices()

        output_line_1 = DashedLine(output_R_vertices[0], output_B_vertices[0])
        output_line_2 = DashedLine(output_R_vertices[1], output_B_vertices[1])
        output_line_3 = DashedLine(output_R_vertices[2], output_B_vertices[2])
        output_line_4 = DashedLine(output_R_vertices[3], output_B_vertices[3])

        output_group = VGroup(output_B, output_G, output_R, output_line_1, output_line_2, output_line_3, output_line_4)

        filter_R = Square(side_length=1.5, fill_opacity=0, stroke_opacity=0.9, color=WHITE)
        filter_R.next_to(input_R, UP + LEFT, buff=-1.5)
        filter_G = Square(side_length=1.5, fill_opacity=0, stroke_opacity=0.75, color=WHITE)
        filter_G.next_to(input_G, UP + LEFT, buff=-1.5)
        filter_G.shift(IN*0.2)
        filter_B = Square(side_length=1.5, fill_opacity=0, stroke_opacity=0.6, color=WHITE)
        filter_B.next_to(input_B, UP + LEFT, buff=-1.5)
        filter_B.shift(IN*0.4)
    
        filter_R_vertices = filter_R.get_vertices()
        filter_B_vertices = filter_B.get_vertices()

        filter_line_1 = DashedLine(filter_R_vertices[0], filter_B_vertices[0])
        filter_line_2 = DashedLine(filter_R_vertices[1], filter_B_vertices[1])
        filter_line_3 = DashedLine(filter_R_vertices[2], filter_B_vertices[2])
        filter_line_4 = DashedLine(filter_R_vertices[3], filter_B_vertices[3])

        filter_group = VGroup(filter_B, filter_G, filter_R, filter_line_1, filter_line_2, filter_line_3, filter_line_4)

        conv_line_1 = DashedLine(filter_R_vertices[0], output_B_vertices[0])
        conv_line_2 = DashedLine(filter_R_vertices[1], output_B_vertices[1])
        conv_line_3 = DashedLine(filter_R_vertices[2], output_B_vertices[2])
        conv_line_4 = DashedLine(filter_R_vertices[3], output_B_vertices[3])

        conv_group = VGroup(filter_group, output_group, conv_line_1, conv_line_2, conv_line_3, conv_line_4)

        CONV_SHIFT_H = 1/4
        CONV_SHIFT_V = 1/4
        
        self.play(FadeIn(rgb_group))
        self.move_camera(phi=PHI_CONV, theta=THETA_CONV, gamma=GAMMA_CONV)
        self.play(input_B.animate.shift(IN*0.4), input_B_label.animate.shift(IN*0.4),
                  input_G.animate.shift(IN*0.2), input_G_label.animate.shift(IN*0.2))
        self.play(FadeIn(conv_group))

        #define feature_map_ind_group
        feature_map_ind_group = VGroup()
        
        #first conv layer
        for y in range(11):
            for x in range(10):
                #leave behind a value
                result_R = output_R.copy()
                result_G = output_G.copy()
                result_B = output_B.copy()
                feature_map_ind_group.add(result_B, result_G, result_R)

                self.add(result_B, result_G, result_R)
                #shift
                self.play(conv_group.animate.shift(RIGHT*CONV_SHIFT_H), run_time=0.01)

            if y < 10:
                self.play(conv_group.animate.shift(LEFT*10*CONV_SHIFT_H), run_time=0.01)
                self.play(conv_group.animate.shift(DOWN*CONV_SHIFT_V), run_time=0.01)
        
        self.play(Uncreate(conv_group))
        self.play(FadeOut(rgb_group))
        self.play(FadeOut(feature_map_ind_group), FadeIn(feature_map_group))
        self.move_camera(phi=PHI_OG, theta=THETA_OG, gamma=GAMMA_OG)
        self.play(feature_map_B.animate.next_to(feature_map_G, LEFT, buff=0.1), 
                  feature_map_R.animate.next_to(feature_map_G, RIGHT, buff=0.1))

        feature_map_R_label.move_to(feature_map_R)
        feature_map_G_label.move_to(feature_map_G)
        feature_map_B_label.move_to(feature_map_B)

        self.play(Write(feature_map_R_label), Write(feature_map_G_label), Write(feature_map_B_label))
        self.wait()
        self.play(Uncreate(feature_map_R_label), Uncreate(feature_map_G_label), Uncreate(feature_map_B_label))
        self.play(feature_map_B.animate.move_to(feature_map_G),
                  feature_map_R.animate.move_to(feature_map_G))
        
        feature_map_B.shift(IN*0.2)
        feature_map_R.shift(OUT*0.2)

        self.move_camera(phi=PHI_CONV, theta=THETA_CONV, gamma=GAMMA_CONV)

class Reconstruction(ThreeDScene):
    def construct(self):
        input_R = Square(side_length=4, color=RED, fill_opacity=0.9)
        input_R_label = Text("HR Patch R").scale(0.6)
        input_R_label.move_to(input_R)
        input_G = Square(side_length=4, color=GREEN, fill_opacity=0.75)
        input_G_label = Text("HR Patch G").scale(0.6)
        input_G_label.move_to(input_G)
        input_B = Square(side_length=4, color=BLUE, fill_opacity=0.6)
        input_B_label = Text("HR Patch B").scale(0.6)
        input_B_label.move_to(input_B)

        rgb_group = VGroup(input_B, input_B_label, input_G, input_G_label, input_R, input_R_label)
        rgb_group.shift(IN*4)

        feature_map_R = Square(side_length=2.5, fill_opacity=0.9, color=RED)   
        feature_map_R_label = Text("HR Patch R").scale(0.6)
        feature_map_G = Square(side_length=2.5, fill_opacity=0.75, color=GREEN)
        feature_map_G.shift(IN*0.2)
        feature_map_G_label = Text("HR Patch G").scale(0.6)
        feature_map_B = Square(side_length=2.5, fill_opacity=0.6, color=BLUE)
        feature_map_B.shift(IN*0.4)
        feature_map_B_label = Text("HR Patch B").scale(0.6)

        feature_map_group = VGroup(feature_map_B, feature_map_G, feature_map_R)

        output_R = Square(side_length=1/5, fill_opacity=0, stroke_opacity=0.9, color=WHITE) 
        output_R.next_to(feature_map_R, UP + LEFT, buff=-1/5)  
        output_G = Square(side_length=1/5, fill_opacity=0, stroke_opacity=0.75, color=WHITE)   
        output_G.next_to(feature_map_G, UP + LEFT, buff=-1/5)
        output_B = Square(side_length=1/5, fill_opacity=0, stroke_opacity=0.6, color=WHITE)   
        output_B.next_to(feature_map_B, UP + LEFT, buff=-1/5)

        output_R_vertices = output_R.get_vertices()
        output_B_vertices = output_B.get_vertices()

        output_line_1 = DashedLine(output_R_vertices[0], output_B_vertices[0])
        output_line_2 = DashedLine(output_R_vertices[1], output_B_vertices[1])
        output_line_3 = DashedLine(output_R_vertices[2], output_B_vertices[2])
        output_line_4 = DashedLine(output_R_vertices[3], output_B_vertices[3])

        output_group = VGroup(output_B, output_G, output_R, output_line_1, output_line_2, output_line_3, output_line_4)

        filter_R = Square(side_length=1.5, fill_opacity=0, stroke_opacity=0.9, color=WHITE)
        filter_R.next_to(input_R, UP + LEFT, buff=-1.5)
        filter_G = Square(side_length=1.5, fill_opacity=0, stroke_opacity=0.75, color=WHITE)
        filter_G.next_to(input_G, UP + LEFT, buff=-1.5)
        filter_G.shift(IN*0.2)
        filter_B = Square(side_length=1.5, fill_opacity=0, stroke_opacity=0.6, color=WHITE)
        filter_B.next_to(input_B, UP + LEFT, buff=-1.5)
        filter_B.shift(IN*0.4)
    
        filter_R_vertices = filter_R.get_vertices()
        filter_B_vertices = filter_B.get_vertices()

        filter_line_1 = DashedLine(filter_R_vertices[0], filter_B_vertices[0])
        filter_line_2 = DashedLine(filter_R_vertices[1], filter_B_vertices[1])
        filter_line_3 = DashedLine(filter_R_vertices[2], filter_B_vertices[2])
        filter_line_4 = DashedLine(filter_R_vertices[3], filter_B_vertices[3])

        filter_group = VGroup(filter_B, filter_G, filter_R, filter_line_1, filter_line_2, filter_line_3, filter_line_4)

        conv_line_1 = DashedLine(filter_R_vertices[0], output_B_vertices[0])
        conv_line_2 = DashedLine(filter_R_vertices[1], output_B_vertices[1])
        conv_line_3 = DashedLine(filter_R_vertices[2], output_B_vertices[2])
        conv_line_4 = DashedLine(filter_R_vertices[3], output_B_vertices[3])

        conv_group = VGroup(filter_group, output_group, conv_line_1, conv_line_2, conv_line_3, conv_line_4)

        CONV_SHIFT_H = 1/4
        CONV_SHIFT_V = 1/4

        input_B.shift(IN*0.4) 
        input_B_label.shift(IN*0.4)
        input_G.shift(IN*0.2)
        input_G_label.shift(IN*0.2)

        self.move_camera(phi=PHI_CONV, theta=THETA_CONV, gamma=GAMMA_CONV)
        self.play(FadeIn(rgb_group, conv_group))
        self.wait()
        self.play(FadeOut(rgb_group), FadeOut(output_group), FadeOut(conv_line_1, conv_line_2,
                                                                     conv_line_3, conv_line_4))
                          #output_group, conv_line_1, conv_line_2, conv_line_3, conv_line_4))
        self.play(filter_group.animate.move_to(ORIGIN))
        self.move_camera(phi=PHI_OG, theta=THETA_OG, gamma=GAMMA_OG)

        filter_label = Text("Reconstruction Filters").scale(0.6)
        filter_label.next_to(feature_map_group, DOWN, buff=0.2)

        self.play(Write(filter_label))
        self.play(filter_group.animate.shift(LEFT*3), filter_label.animate.shift(LEFT*3))
        self.wait()

        domain_label = Text(r"IS = Image-Space Domain, FS = Feature-Space Domain", color=YELLOW).scale(0.6)
        domain_label.shift(DOWN*3.2)

        feature_space = Circle(color=RED, fill_opacity=0.5).scale(0.5)
        feature_space_label = Text("FS").scale(0.8)
        feature_space_label.move_to(feature_space)
        feature_space_group = VGroup(feature_space, feature_space_label)
        feature_space_group.shift(RIGHT*3 + UP*1)

        image_space = Circle(radius=1.5, color=BLUE, fill_opacity=0.5)
        image_space_label = Text("IS").scale(0.8)
        image_space_label.next_to(image_space, UP, buff=-0.75)
        image_space_group = VGroup(image_space, image_space_label)
        image_space_group.shift(RIGHT*3 + UP*1.5)

        avg_patches = MathTex(r"\frac{1}{N}\sum_{i=1}^{N}{\text{HR Patch}}_i", font_size=36)
        avg_patches.next_to(image_space_group, DOWN, buff=1)

        proj_arrow = Arrow(filter_group.get_edge_center(RIGHT), image_space_group.get_edge_center(LEFT), stroke_width=4)
        avg_arrow = Arrow(image_space_group.get_edge_center(DOWN), avg_patches.get_edge_center(UP), stroke_width=4)

        self.play(Create(proj_arrow))
        self.play(Write(domain_label), FadeIn(image_space_group), FadeIn(feature_space_group))
        self.play(Create(avg_arrow))
        self.play(Write(avg_patches))
        self.wait()

        self.play(FadeOut(image_space_group, feature_space_group, avg_patches, proj_arrow, avg_arrow))
        self.play(Create(proj_arrow))

        feature_space_group.shift(UP*2 + LEFT*2)

        self.play(FadeIn(image_space_group), FadeIn(feature_space_group))
        self.play(feature_space_group.animate.shift(DOWN*2 + RIGHT*2))
        self.play(Create(avg_arrow))
        self.play(Write(avg_patches))
        self.wait()

        
