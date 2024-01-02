from manim import *

class NonUnique(ThreeDScene):
    def construct(self):
        LR = Square(color=GRAY, fill_opacity=0.5)
        LR.shift(LEFT*3)
        LR_label = Text("Low Res").scale(0.6)
        LR_label.move_to(LR)

        F_mapping = Circle(color=ORANGE, fill_opacity=0.5).scale(0.5)
        F_mapping_label = Text("F", color=WHITE, slant=ITALIC).scale(0.6)

        HR = Square(side_length=1.5, color=GREEN, fill_opacity=0.5)
        HR.shift(RIGHT*3)
        HR_label = Text("High Res").scale(0.4)
        HR_label.move_to(HR)
        HR_group = VGroup(HR, HR_label)

        HR_1 = HR_group.copy()
        HR_2 = HR_group.copy()
        HR_3 = HR_group.copy()

        START_POINT = F_mapping.get_edge_center(RIGHT)

        line_across_L = Line(LR.get_edge_center(RIGHT), F_mapping.get_edge_center(LEFT), color=WHITE)
        line_across_R_0 = Line(START_POINT, HR_group.get_edge_center(LEFT), color=WHITE)

        self.play(FadeIn(F_mapping), FadeIn(F_mapping_label), FadeIn(LR), FadeIn(LR_label), Create(line_across_L))
        self.wait()
        self.play(Create(line_across_R_0), FadeIn(HR_group))
        self.play(HR_group.animate.shift(UP), 
                  line_across_R_0.animate.put_start_and_end_on(START_POINT, HR_group.get_edge_center(LEFT) + UP))

        HR_1.next_to(HR_group, DOWN, buff=0.2)
        HR_2.next_to(HR_group, UP, buff=0.2)
        HR_3.next_to(HR_1, DOWN, buff=0.2)
        line_across_R_1 = Line(START_POINT, HR_1.get_edge_center(LEFT), color=WHITE)
        line_across_R_2 = Line(START_POINT, HR_2.get_edge_center(LEFT), color=WHITE)
        line_across_R_3 = Line(START_POINT, HR_3.get_edge_center(LEFT), color=WHITE)

        self.play(Create(line_across_R_1), FadeIn(HR_1))
        self.play(Create(line_across_R_2), FadeIn(HR_2))
        self.play(Create(line_across_R_3), FadeIn(HR_3))
        self.wait()

        HR_best = Square(color=BLUE, fill_opacity=0.5)
        HR_best.shift(RIGHT*3)
        HR_best_label = Text("HR Output").scale(0.6)
        HR_best_label.move_to(HR_best)
        HR_best_group = VGroup(HR_best, HR_best_label)

        self.play(FadeOut(HR_group, HR_1, HR_2, HR_3), 
                  line_across_R_0.animate.put_start_and_end_on(START_POINT, HR_best_group.get_edge_center(LEFT)),
                  line_across_R_1.animate.put_start_and_end_on(START_POINT, HR_best_group.get_edge_center(LEFT)),
                  line_across_R_2.animate.put_start_and_end_on(START_POINT, HR_best_group.get_edge_center(LEFT)),
                  line_across_R_3.animate.put_start_and_end_on(START_POINT, HR_best_group.get_edge_center(LEFT)),
                  FadeIn(HR_best_group)
                  )
        self.wait()
        
        q_mark = MathTex(r"?", font_size=64)
        q_mark.next_to(HR_best_group, UP, buff=0.1)

        self.play(Write(q_mark))
        self.wait()
