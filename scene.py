from manim import *
import numpy as np
import math

class PartOne(Scene):
    def construct(self):
        degredation = MathTex(r"I_x = D(I_y; \delta)", font_size=64)
        regeneration = MathTex(r"\hat{I_y} = F(I_x; \theta)", font_size=64)
        part_one = VGroup(degredation, regeneration).arrange(DOWN)

        self.add(part_one)

class PartTwo(Scene):
    def construct(self):
        mse = MathTex(r"MSE = \frac{1}{mn}\sum_{i=0}^{m-1}\sum_{j=0}^{n-1}[X(i,j) - Y(i,j)]^2", font_size=64)
        psnr = MathTex(r"10log_{10}\left(\frac{{MAX_I}^2}{MSE}\right)", font_size=64)

        self.add(mse)

class SSIM(Scene):
    def construct(self):
        luminance = MathTex(r"Luminance = \mu_x = \frac{1}{N}\sum_{i=1}^Nx_i")
        contrast = MathTex(r"Contrast = \sigma_x = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \mu_x)^2}", font_size=64)
        sigma_xy = MathTex(r"\sigma_{xy} = \frac{1}{N-1}\sum_{i=1}^{N}(x_i - \mu_i)(y_i - \mu_y)", font_size=64)
        l_comp = MathTex(r"l(x,y) = \frac{2\mu_x\mu_y + C_1}{{\mu_x}^2 + {\mu_y}^2 + C_1}", font_size=64)
        c_comp = MathTex(r"c(x,y) = \frac{2\sigma_x\sigma_y + C_2}{{\sigma_x}^2 + {\sigma_y}^2 + C_2}", font_size=64)
        s_comp = MathTex(r"s(x,y) = \frac{\sigma_{xy} + C_3}{\sigma_x\sigma_y + C_3}", font_size=64)
        ssim = MathTex(r"SSIM(x,y) = [l(x,y)]^{\alpha}[c(x,y)]^{\beta}[s(x,y)]^{\gamma}", font_size=64)
        ssim_cond = MathTex(r"where\ (\alpha, \beta, \gamma) > 0")
        ssim_group = VGroup(ssim, ssim_cond).arrange(DOWN)
        mssim = MathTex(r"MSSIM(X,Y) = \frac{1}{M}\sum_{j=1}^{M}SSIM(x_j, y_j)", font_size=64)

        self.add(mssim)

class PartThree(Scene):
    def construct(self):
        layer_one = MathTex(r"F_1(Y) = max(0, W_1*Y + B_1)", font_size=64)
        layer_two = MathTex(r"F_2(Y) = max(0, W_2*F_1(Y) + B_2)", font_size=64)
        layer_three = MathTex(r"F(Y) = W_3*F_2(Y) + B_3", font_size=64)

        self.add(layer_three)

class InfoTheory(Scene):
    def construct(self):
        #create elements
        LR = Square(color=GREEN, fill_opacity=0.5)
        LR.shift(LEFT*3)
        LR_label = Text("Low Res").scale(0.6)
        LR_label.move_to(LR)

        F_mapping = Circle(color=RED, fill_opacity=0.5).scale(0.5)
        F_mapping_label = Text("F", color=WHITE, slant=ITALIC).scale(0.6)

        HR_lower = Square(color=BLUE, fill_opacity=0.5)
        HR_lower.shift(RIGHT*3)
        HR_lower_label = Text("High Res").scale(0.6)
        HR_lower_label.move_to(HR_lower)

        HR_upper = Square(color=BLUE, fill_opacity=0.5)
        HR_upper.shift(RIGHT*3)
        HR_upper.shift(UP*1.5)
        HR_upper_label = Text("High Res \n + Info").scale(0.6)
        HR_upper_label.move_to(HR_upper)

        NN = Circle(color=GRAY, fill_opacity=0.5).scale(0.5)
        NN.shift(UP*2)
        NN_label = Text("NN").scale(0.8)
        NN_label.move_to(NN)

        line_across_L = Line(LR.get_edge_center(RIGHT), F_mapping.get_edge_center(LEFT), color=WHITE)
        line_across_R_down = Line(F_mapping.get_edge_center(RIGHT), HR_lower.get_edge_center(LEFT), color=WHITE)
        line_across_R_up = Line(F_mapping.get_edge_center(RIGHT), HR_upper.get_edge_center(LEFT), color=WHITE)


        # Angle in radians corresponding to 45 degrees
        start_point = NN.get_center() + RIGHT*0.35 + DOWN*0.35
        arrow = Line(start_point, line_across_R_up.get_center())
        #arrow_down = Arrow(NN.get_center(), DOWN, buff=0.8, color=WHITE)

        #horizontal group for standard process
        #standard_group = VGroup(LR, LR_label, line_across_L, F_mapping, line_across_R, HR_lower, HR_lower_label)

        #animation
        self.play(FadeIn(F_mapping), Write(F_mapping_label))
        self.play(FadeIn(LR), Write(LR_label))
        self.play(Create(line_across_L))
        self.wait()
        self.play(Create(line_across_R_down))
        self.play(FadeIn(HR_lower), Write(HR_lower_label))
        self.play(HR_lower.animate.shift(DOWN*1.5), HR_lower_label.animate.shift(DOWN*1.5), 
                  line_across_R_down.animate.put_start_and_end_on(F_mapping.get_edge_center(RIGHT), 
                  HR_lower.get_edge_center(LEFT) + DOWN * 1.5))
        self.play(FadeIn(NN), Write(NN_label))
        self.play(Create(line_across_R_up), Create(arrow))
        self.play(FadeIn(HR_upper), Write(HR_upper_label))
        #self.play(Create(line_across_L))
        #self.play(Write(line_label))
        #self.play(Create(line_across_R))
        #self.play(standard_group.animate.shift(DOWN), FadeIn(NN), Write(NN_label))
        #self.play(Create(arrow_down))
        

