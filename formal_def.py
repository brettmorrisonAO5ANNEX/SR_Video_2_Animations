from manim import *

class FormalDef(Scene):
    def construct(self):
        standard = ImageMobject("assets/Willy-Standard.png").scale(0.15)
        standard.shift(RIGHT*3)
        standard_label = Text("High Res Counterpart").scale(0.6)
        standard_label.next_to(standard, DOWN, buff=0.1)

        pixelated = ImageMobject("assets/Willy-Pixelated.png").scale(0.15)
        pixelated.shift(LEFT*3)
        pixelated_label = Text("Low Res Image").scale(0.6)
        pixelated_label.next_to(pixelated, DOWN, buff=0.1)

        image_arrow = Arrow(pixelated.get_edge_center(RIGHT), standard.get_edge_center(LEFT))

        self.play(FadeIn(pixelated, pixelated_label))
        self.wait()
        self.play(Create(image_arrow))
        self.play(FadeIn(standard, standard_label))
        self.wait()
        self.play(FadeOut(standard, standard_label), FadeOut(image_arrow), FadeOut(pixelated, pixelated_label))
        self.wait()

        degredation_group = VGroup()

        OG = Square(color=YELLOW, fill_opacity=0.5)
        OG.shift(LEFT*3)
        OG_label = MathTex(r"I_y", font_size=64)
        OG_label.move_to(OG)
        GT_label = Text("Ground Truth").scale(0.6)
        GT_label.next_to(OG, UP, buff=0.1)
        degredation_group.add(OG, OG_label, GT_label)

        D_mapping = Circle(color=ORANGE, fill_opacity=0.5).scale(0.5)
        D_mapping_label = MathTex(r"D", font_size=64)
        degredation_group.add(D_mapping, D_mapping_label)

        D_mapping_params = Circle(color=WHITE, fill_opacity=0.5).scale(0.5)
        D_mapping_params_label = MathTex(r"\delta", font_size=64)
        D_mapping_params.shift(UP*2)
        D_mapping_params_label.shift(UP*2)
        degredation_group.add(D_mapping_params, D_mapping_params_label)

        DG = Square(color=GRAY, fill_opacity=0.5)
        DG.shift(RIGHT*3)
        DG_label = MathTex(r"I_x", font_size=64)
        DG_label.move_to(DG)
        LowR_label = Text("Low Res").scale(0.6)
        LowR_label.next_to(DG, UP, buff=0.1)

        degredation = MathTex(r"I_x = D(I_y; \delta)", font_size=64)
        degredation_group.add(degredation)

        self.play(Write(degredation))
        self.wait()
        self.play(degredation.animate.shift(DOWN*2))
        self.wait()
        self.play(FadeIn(D_mapping, D_mapping_label))
        self.wait()
        self.play(FadeIn(D_mapping_params, D_mapping_params_label))
        self.wait()  
        self.play(FadeIn(OG, OG_label), Write(GT_label))

        param_connection = Arrow(D_mapping_params.get_edge_center(DOWN), D_mapping.get_edge_center(UP))
        input_connection = Line(OG.get_edge_center(RIGHT), D_mapping.get_edge_center(LEFT))
        output_connection = Line(D_mapping.get_edge_center(RIGHT), DG.get_edge_center(LEFT))
        degredation_group.add(param_connection, input_connection, output_connection)

        self.play(Create(param_connection))
        self.play(Create(input_connection))
        self.play(Create(output_connection))
        self.play(FadeIn(DG, DG_label), Write(LowR_label))
        self.wait()
        self.play(FadeOut(degredation_group))
        self.wait()

        HR_output = Square(color=BLUE, fill_opacity=0.5)
        HR_output.shift(RIGHT*3)
        HR_output_label = MathTex(r"\hat{I_y}", font_size=64)
        HR_output_label.move_to(HR_output)
        HR_top_label = Text("High Res Output").scale(0.6)
        HR_top_label.next_to(HR_output, UP, buff=0.1)

        F_mapping = Circle(color=ORANGE, fill_opacity=0.5).scale(0.5)
        F_mapping_label = MathTex(r"F", font_size=64)

        F_mapping_params = Circle(color=WHITE, fill_opacity=0.5).scale(0.5)
        F_mapping_params_label = MathTex(r"\theta", font_size=64)
        F_mapping_params.shift(UP*2)
        F_mapping_params_label.shift(UP*2)

        regeneration = MathTex(r"\hat{I_y} = F(I_x; \theta)", font_size=64)
        regeneration.shift(DOWN*2)

        self.play(DG.animate.shift(LEFT*6), DG_label.animate.shift(LEFT*6), LowR_label.animate.shift(LEFT*6), Write(regeneration))
        self.wait()
        self.play(FadeIn(F_mapping, F_mapping_label))
        self.wait()
        self.play(FadeIn(F_mapping_params, F_mapping_params_label))
        self.wait()

        param_connection = Arrow(F_mapping_params.get_edge_center(DOWN), F_mapping.get_edge_center(UP))
        input_connection = Line(DG.get_edge_center(RIGHT), F_mapping.get_edge_center(LEFT))
        output_connection = Line(F_mapping.get_edge_center(RIGHT), HR_output.get_edge_center(LEFT))

        self.play(Create(param_connection))
        self.play(Create(input_connection))
        self.play(Create(output_connection))
        self.play(FadeIn(HR_output, HR_output_label), Write(HR_top_label))
        self.wait()