from manim import *

class QM2(ThreeDScene):
    def construct(self):
        PHI_OG = 0*DEGREES
        THETA_OG = -90*DEGREES
        GAMMA_OG = 0*DEGREES
        PHI_CONV = -75*DEGREES
        THETA_CONV = 0*DEGREES
        GAMMA_CONV = 90*DEGREES

        Input = Square(color=GRAY, fill_opacity=0.5)
        Input.shift(LEFT*3)
        Input_label = Text("Low Res").scale(0.6)
        Input_label.move_to(Input)
        Input_Group = VGroup(Input, Input_label)

        Quality_metric = Circle(color=ORANGE, fill_opacity=0.5).scale(0.5)
        Quality_metrics_label = Text("QM").scale(0.6)
        Quality_metrics_label.move_to(Quality_metric)
        QM_group = VGroup(Quality_metric, Quality_metrics_label)

        Full_ref = Square(color=YELLOW, fill_opacity=0.5).scale(0.8)
        Full_ref.shift(DOWN*2)
        Full_ref_label = Text("Full Ref").scale(0.6)
        Full_ref_label.move_to(Full_ref)
        Full_ref_group = VGroup(Full_ref, Full_ref_label)

        vertices_upper = [
            [-0.8, 0.8, 0],
            [0.8, 0.8, 0],
            [0.8, -0.8, 0]
        ]

        vertices_lower = [
            [-0.8, 0.8, 0],
            [-0.8, -0.8, 0],
            [0.8, -0.8, 0]
        ]

        # Create a right triangle using Polygon
        Partial_ref = Polygon(*vertices_lower, color=YELLOW, fill_opacity=0.5)
        Partial_ref_upper = Polygon(*vertices_upper, color=YELLOW, fill_opacity=0)
        Partial_ref.shift(DOWN*2)
        Partial_ref_upper.shift(DOWN*2)
        Partial_ref_label = Text("Part Ref").scale(0.6)
        Partial_ref_label.move_to(Partial_ref)
        Partial_ref_group = VGroup(Partial_ref, Partial_ref_upper, Partial_ref_label)

        No_ref = Square(color=YELLOW, fill_opacity=0).scale(0.8)
        No_ref.shift(DOWN*2)
        No_ref_label = Text("No Ref").scale(0.6)
        No_ref_label.move_to(No_ref)
        No_ref_group = VGroup(No_ref, No_ref_label)

        output_label = Text("quality metric").scale(0.6)
        output_label.shift(RIGHT*3)
        output_label_box = SurroundingRectangle(output_label, color=WHITE, fill_opacity=0)
        output_group = VGroup(output_label_box, output_label)

        in_qm_line = Line(Input_Group.get_edge_center(RIGHT), QM_group.get_edge_center(LEFT))
        ref_qm_line = Line(Full_ref_group.get_edge_center(UP), QM_group.get_edge_center(DOWN))
        output_arrow = Line(QM_group.get_edge_center(RIGHT), output_group.get_edge_center(LEFT))

        label_1 = Text("Full-Reference", font_size=64)
        label_1.shift(UP*2)
        label_2 = Text("Partial-Reference", font_size=64)
        label_2.shift(UP*2)
        label_3 = Text("Blind", font_size=64)
        label_3.shift(UP*2)

        self.play(FadeIn(Input_Group, QM_group))
        self.play(FadeIn(Full_ref_group), Create(in_qm_line), Create(ref_qm_line), FadeIn(label_1))
        self.play(Create(output_arrow), FadeIn(output_group))
        self.wait()
        self.play(Transform(Full_ref_group, Partial_ref_group), Transform(label_1, label_2))
        self.wait()
        self.play(Transform(Full_ref_group, No_ref_group), Transform(label_1, label_3))
        self.wait()
        self.play(FadeOut(Input_Group, in_qm_line, QM_group, ref_qm_line, output_arrow, Full_ref_group, output_group, label_1))

        input_RGB = Square(side_length=4, color=BLUE, fill_opacity=0.5)
        input_RGB_label = Text("RGB").scale(0.6)
        input_RGB_label.move_to(input_RGB)
        input_RGB_group = VGroup(input_RGB, input_RGB_label)
        input_RGB_group.shift(LEFT*2.5)

        input_R = Square(side_length=4, color=RED, fill_opacity=0.9)
        input_R_label = Text("R").scale(0.6)
        input_R_label.move_to(input_R)
        input_G = Square(side_length=4, color=GREEN, fill_opacity=0.75)
        input_G_label = Text("G").scale(0.6)
        input_G_label.move_to(input_G)
        input_B = Square(side_length=4, color=BLUE, fill_opacity=0.6)
        input_B_label = Text("B").scale(0.6)
        input_B_label.move_to(input_B)

        rgb_group = VGroup(input_B, input_B_label, input_G, input_G_label, input_R, input_R_label)
        rgb_group.shift(IN*2)

        grayscale = Square(side_length=4, color=GRAY, fill_opacity=0.5)
        grayscale_label = Text("Grayscale").scale(0.6)
        grayscale_label.move_to(grayscale)

        grayscale_group = VGroup(grayscale, grayscale_label)
        grayscale_group.shift(RIGHT*2.5)
        #rgb_group.shift(IN*4)

        self.play(FadeIn(input_RGB_group), FadeIn(grayscale_group))
        self.wait()
        self.move_camera(phi=PHI_CONV, theta=THETA_CONV, gamma=GAMMA_CONV)
        self.play(input_RGB_group.animate.shift(RIGHT*2.5 + IN*2), grayscale_group.animate.shift(LEFT*2.5 + OUT*2))
        self.play(FadeOut(input_RGB_group), FadeIn(rgb_group))
        self.play(input_B.animate.shift(IN*0.4), input_B_label.animate.shift(IN*0.4),
                  input_G.animate.shift(IN*0.2), input_G_label.animate.shift(IN*0.2))