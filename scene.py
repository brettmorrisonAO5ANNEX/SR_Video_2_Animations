from manim import *
import numpy as np
import math

#global elemnts
Willy_standard = ImageMobject("assets/Willy-Standard.png").scale(0.1)
Willy_pixelated = ImageMobject("assets/Willy-Pixelated.png").scale(0.1)
Willy_square = ImageMobject("assets/Willy-Square.png").scale(0.1)

class Intro(Scene):
    def construct(self):
        Title = Text("Image Super-Resolution Series", font_size=64)
        SubTitle = Text("Video 2: Topic Overview", font_size=36, color=GREEN)
        SubTitle.next_to(Title, DOWN, buff=0.1)

        self.play(Write(Title))
        self.wait()
        self.play(Write(SubTitle))
        self.wait()
        self.play(FadeOut(Title), SubTitle.animate.shift(UP*0.5))

class InfoTheory(Scene):
    def construct(self):
        LR = Square(color=GRAY, fill_opacity=0.5)
        LR.shift(LEFT*3)
        LR_label = Text("Low Res").scale(0.6)
        LR_label.move_to(LR)

        F_mapping = Circle(color=ORANGE, fill_opacity=0.5).scale(0.5)
        F_mapping_label = Text("F", color=WHITE, slant=ITALIC).scale(0.6)

        HR = Square(color=GREEN, fill_opacity=0.5)
        HR.shift(RIGHT*3)
        HR_label = Text("High Res 1").scale(0.6)
        HR_label.move_to(HR)

        HR_upper = Square(color=BLUE, fill_opacity=0.5)
        HR_upper.shift(RIGHT*3)
        HR_upper.shift(UP*1.5)
        HR_upper_label = Text("High Res 2").scale(0.6)
        HR_upper_label.move_to(HR_upper)

        NN = Circle(color=ORANGE, fill_opacity=0.5).scale(0.5)
        NN.shift(UP*2)
        NN_label = Text("NN").scale(0.8)
        NN_label.move_to(NN)

        line_across_L = Line(LR.get_edge_center(RIGHT), F_mapping.get_edge_center(LEFT), color=WHITE)
        line_across_R_down = Line(F_mapping.get_edge_center(RIGHT), HR.get_edge_center(LEFT), color=WHITE)
        line_across_R_up = Line(F_mapping.get_edge_center(RIGHT), HR_upper.get_edge_center(LEFT), color=WHITE)

        # Angle in radians corresponding to 45 degrees
        start_point = NN.get_center() + RIGHT*0.35 + DOWN*0.35
        arrow = Line(start_point, line_across_R_up.get_center())

        self.play(FadeIn(F_mapping), Write(F_mapping_label))
        self.play(FadeIn(LR), Write(LR_label))
        self.play(Create(line_across_L))
        self.wait()
        self.play(Create(line_across_R_down))
        self.play(FadeIn(HR), Write(HR_label))
        self.play(HR.animate.shift(DOWN*1.5), HR_label.animate.shift(DOWN*1.5), 
                  line_across_R_down.animate.put_start_and_end_on(F_mapping.get_edge_center(RIGHT), 
                  HR.get_edge_center(LEFT) + DOWN * 1.5))
        self.play(FadeIn(NN), Write(NN_label))
        self.play(Create(line_across_R_up), Create(arrow))
        self.play(FadeIn(HR_upper), Write(HR_upper_label))

class FormalDef(Scene):
    def construct(self):
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
        degredation.shift(DOWN*2)
        degredation_group.add(degredation)

        self.play(FadeIn(OG, OG_label), FadeIn(D_mapping, D_mapping_label), Write(GT_label))
        self.play(FadeIn(D_mapping_params, D_mapping_params_label))

        param_connection = Arrow(D_mapping_params.get_edge_center(DOWN), D_mapping.get_edge_center(UP))
        input_connection = Line(OG.get_edge_center(RIGHT), D_mapping.get_edge_center(LEFT))
        output_connection = Line(D_mapping.get_edge_center(RIGHT), DG.get_edge_center(LEFT))
        degredation_group.add(param_connection, input_connection, output_connection)

        self.play(Create(param_connection))
        self.play(Create(input_connection))
        self.play(Create(output_connection))
        self.play(FadeIn(DG, DG_label), Write(LowR_label))
        self.play(Write(degredation))
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

        self.play(DG.animate.shift(LEFT*6), DG_label.animate.shift(LEFT*6), LowR_label.animate.shift(LEFT*6),
                  FadeIn(F_mapping, F_mapping_label))
        self.play(FadeIn(F_mapping_params, F_mapping_params_label))

        param_connection = Arrow(F_mapping_params.get_edge_center(DOWN), F_mapping.get_edge_center(UP))
        input_connection = Line(DG.get_edge_center(RIGHT), F_mapping.get_edge_center(LEFT))
        output_connection = Line(F_mapping.get_edge_center(RIGHT), HR_output.get_edge_center(LEFT))

        self.play(Create(param_connection))
        self.play(Create(input_connection))
        self.play(Create(output_connection))
        self.play(FadeIn(HR_output, HR_output_label), Write(HR_top_label))
        self.play(Write(regeneration))
        self.wait()

class QualityMetrics(Scene):
    def construct(self):  
        Loc_Willy_standard = Willy_standard
        Loc_Willy_pixelated = Willy_pixelated
        Loc_Willy_pixelated.shift(RIGHT*4)  

        mse = MathTex(r"MSE = \frac{1}{mn}\sum_{i=0}^{m-1}\sum_{j=0}^{n-1}[X(i,j) - Y(i,j)]^2", font_size=64)

        left_bracket = Brace(Loc_Willy_standard, direction=LEFT)
        left_bracket.next_to(Loc_Willy_standard, LEFT)
        right_bracket = Brace(Loc_Willy_pixelated, direction=RIGHT)
        right_bracket.next_to(Loc_Willy_pixelated, RIGHT)

        subtraction_symbol = MathTex("-", font_size=64)
        subtraction_symbol.next_to(Loc_Willy_standard, RIGHT)
        subtraction_symbol.next_to(Loc_Willy_pixelated, LEFT)

        squared_symbol = MathTex(r"2", font_size=64)
        squared_symbol.next_to(right_bracket, UP, buff=-0.2)
        squared_symbol.shift(RIGHT*0.3)
        
        sum_symbol = MathTex(r"\sum", font_size=96)
        sum_symbol.next_to(left_bracket, LEFT)

        mse_label = MathTex(r"MSE = ", font_size=64)
        mse_label.next_to(sum_symbol, LEFT)

        GT_label = Text("Ground Truth").scale(0.6)
        GT_label.next_to(Loc_Willy_standard, DOWN)
        OP_label = Text("HR Output").scale(0.6)
        OP_label.next_to(Loc_Willy_pixelated, DOWN)   

        self.play(Write(mse))
        self.wait(2)
        self.play(Transform(mse, mse_label))
        self.play(Write(sum_symbol), Create(left_bracket), 
                  Write(GT_label), Write(subtraction_symbol), Write(OP_label), 
                  Create(right_bracket), Write(squared_symbol))
        self.play(FadeIn(Loc_Willy_standard), FadeIn(Loc_Willy_pixelated))
        self.wait(2)
        self.play(FadeOut(squared_symbol), FadeOut(right_bracket), FadeOut(Willy_pixelated),
                  FadeOut(subtraction_symbol), FadeOut(Willy_standard), FadeOut(left_bracket),
                  FadeOut(sum_symbol), FadeOut(mse), FadeOut(GT_label), FadeOut(OP_label))
        self.wait(2)

        psnr = MathTex(r"PSNR = 10log_{10}\left(\frac{{MAX_I}^2}{MSE}\right)", font_size=64)   
        mse_hypersphere = ImageMobject("assets/MSE-Hypersphere.png").scale(1.5)
        
        self.play(Create(psnr))
        self.wait(2)
        self.play(Uncreate(psnr))
        self.play(FadeIn(mse_hypersphere))
        self.wait(2)
        self.play(FadeOut(mse_hypersphere))

        GT_background = Square(color=YELLOW, fill_opacity=0.5)
        GT_background.shift(RIGHT*2)
        GT_background_label = Text("GT").scale(0.6)
        GT_background_label.move_to(GT_background)

        LR = Square(color=BLUE, fill_opacity=0.5)
        LR.shift(LEFT*2)
        LR_label = Text("HR Output").scale(0.6)
        LR_label.move_to(LR)

        input_group = VGroup(GT_background, GT_background_label, LR, LR_label)

        merged_image = Square(color=GRAY, fill_opacity=0.5)
        merged_image_label=Text("image").scale(0.6)
        merged_image_label.move_to(merged_image)
        merged_image_group = VGroup(merged_image, merged_image_label)

        SHIFT_SCALAR = 0.6

        LR_window_1 = Square(color=GRAY, fill_opacity=0.5).scale(0.5)
        LR_window_1.shift(LEFT*SHIFT_SCALAR)
        LR_window_1.shift(UP*SHIFT_SCALAR)
        W1_label = MathTex(r"W_1", font_size=36)
        W1_label.move_to(LR_window_1)

        LR_window_2 = Square(color=GRAY, fill_opacity=0.5).scale(0.5)
        LR_window_2.shift(RIGHT*SHIFT_SCALAR)
        LR_window_2.shift(UP*SHIFT_SCALAR)
        W2_label = MathTex(r"W_2", font_size=36)
        W2_label.move_to(LR_window_2)

        LR_window_3 = Square(color=GRAY, fill_opacity=0.5).scale(0.5)
        LR_window_3.shift(LEFT*SHIFT_SCALAR)
        LR_window_3.shift(DOWN*SHIFT_SCALAR)
        W3_label = MathTex(r"W_3", font_size=36)
        W3_label.move_to(LR_window_3)

        LR_window_4 = Square(color=GRAY, fill_opacity=0.5).scale(0.5)
        LR_window_4.shift(RIGHT*SHIFT_SCALAR)
        LR_window_4.shift(DOWN*SHIFT_SCALAR)
        W4_label = MathTex(r"W_4", font_size=36)
        W4_label.move_to(LR_window_4)

        top_row = VGroup(LR_window_1, LR_window_2)
        bottom_row = VGroup(LR_window_3, LR_window_4)
        total_windows = VGroup(top_row, bottom_row)

        vertical_slice_front = DashedLine(merged_image.get_edge_center(UP), merged_image.get_edge_center(DOWN), color=RED)
        horizontal_slice_front = DashedLine(merged_image.get_edge_center(LEFT), merged_image.get_edge_center(RIGHT), color=RED)

        bottom_message = MathTex(r"\text{for } i \in \{1, 2, \ldots, n\}, \text{ where n = number of windows, x = ground truth, y = HR output}", font_size=32, color=YELLOW)
        bottom_message.shift(DOWN*3.2)

        WN = Square(color=GRAY, fill_opacity=0.5)
        WN.shift(LEFT*2)
        WN_label =  MathTex(r"W_n^{\{x,y\}}", font_size=48)
        WN_label.move_to(WN)

        self.play(FadeIn(GT_background), Write(GT_background_label), FadeIn(LR), Write(LR_label))
        self.wait()
        self.play(LR.animate.shift(RIGHT*2), LR_label.animate.shift(RIGHT*2),
                  GT_background.animate.shift(LEFT*2), GT_background_label.animate.shift(LEFT*2)) 
        self.play(FadeOut(input_group), FadeIn(merged_image_group))
        self.play(GrowFromCenter(vertical_slice_front), GrowFromCenter(horizontal_slice_front))
        self.play(FadeOut(merged_image_group), FadeIn(total_windows), FadeOut(vertical_slice_front), 
                  FadeOut(horizontal_slice_front), Write(W1_label), Write(W2_label),
                  Write(W3_label), Write(W4_label))
        self.wait(2)
        self.play(FadeOut(W1_label), FadeOut(W2_label),
                  FadeOut(W3_label), FadeOut(W4_label), Transform(total_windows, WN))
        self.play(Write(bottom_message), Write(WN_label))

        sigma = MathTex(r"\sigma_x, \sigma_y", font_size=64, color=WHITE)
        sigma.shift(RIGHT*2)
        sigma_box = SurroundingRectangle(sigma, color=GREEN, fill_opacity=0.5)
        sigma_box.move_to(sigma)
        sigma_group = VGroup(sigma_box, sigma)

        mu = MathTex(r"\mu_x, \mu_y", font_size=64, color=WHITE)
        mu.next_to(sigma, UP, aligned_edge=LEFT, buff=0.5)
        mu_box = SurroundingRectangle(mu, color=RED, fill_opacity=0.5)
        mu_box.move_to(mu)
        mu_group = VGroup(mu_box, mu)

        covariance = MathTex(r"\sigma_{xy}", font_size=64, color=WHITE)
        covariance.next_to(sigma, DOWN, aligned_edge=LEFT, buff=0.5)
        covariance_box = SurroundingRectangle(covariance, color=BLUE, fill_opacity=0.5)
        covariance_box.move_to(covariance)
        covariance_group = VGroup(covariance_box, covariance)

        START_POINT = WN.get_edge_center(RIGHT)

        mu_line = Line(START_POINT, mu_box.get_edge_center(LEFT))
        sigma_line = Line(START_POINT, sigma.get_edge_center(LEFT) + LEFT*0.1)
        covariance_line = Line(START_POINT, covariance.get_edge_center(LEFT) + LEFT*0.1)

        self.play(Create(mu_line))
        self.play(FadeIn(mu_group))
        self.play(Create(sigma_line))
        self.play(FadeIn(sigma_group))
        self.play(Create(covariance_line))
        self.play(FadeIn(covariance_group))
        self.wait(2)

        contrast = MathTex(r"\sigma_{\{x,y\}} = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(\{x,y\}_i - \mu_{\{x,y\}})^2}", font_size=36, color=WHITE)
        contrast_box = SurroundingRectangle(contrast, color=GREEN, fill_opacity=0.5)
        contrast_group = VGroup(contrast_box, contrast)

        luminance = MathTex(r"\mu_{\{x,y\}} = \frac{1}{N}\sum_{i=1}^N\{x,y\}_i", font_size=36, color=WHITE)
        luminance_box = SurroundingRectangle(luminance, color=RED, fill_opacity=0.5)
        luminance_group = VGroup(luminance_box, luminance)
        
        sigma_xy = MathTex(r"\sigma_{xy} = \frac{1}{N-1}\sum_{i=1}^{N}(x_i - \mu_i)(y_i - \mu_y)", font_size=36, color=WHITE)
        sigma_box = SurroundingRectangle(sigma_xy, color=BLUE, fill_opacity=0.5)
        sigma_xy_group = VGroup(sigma_box, sigma_xy)

        contrast_group.shift(RIGHT*2)
        luminance_group.next_to(contrast_group, UP, aligned_edge=LEFT, buff=0.5)
        sigma_xy_group.next_to(contrast_group, DOWN, aligned_edge=LEFT, buff=0.5)

        START_POINT += LEFT*2.5

        self.play(total_windows.animate.shift(LEFT*2.5), WN_label.animate.shift(LEFT*2.5),
                  mu_line.animate.put_start_and_end_on(START_POINT, luminance_box.get_edge_center(LEFT)),
                  sigma_line.animate.put_start_and_end_on(START_POINT, contrast_box.get_edge_center(LEFT)),
                  covariance_line.animate.put_start_and_end_on(START_POINT, sigma_box.get_edge_center(LEFT)),
                  Transform(mu_group, luminance_group), 
                  Transform(sigma_group, contrast_group), 
                  Transform(covariance_group, sigma_xy_group))
        self.wait(2)
        
        c_comp = MathTex(r"c(x,y) = \frac{2\sigma_x\sigma_y + C_2}{{\sigma_x}^2 + {\sigma_y}^2 + C_2}", font_size=36, color=WHITE)
        c_comp_box = SurroundingRectangle(c_comp, color=GREEN, fill_opacity=0.5)
        c_comp_group = VGroup(c_comp_box, c_comp)

        l_comp = MathTex(r"l(x,y) = \frac{2\mu_x\mu_y + C_1}{{\mu_x}^2 + {\mu_y}^2 + C_1}", font_size=36, color=WHITE)
        l_comp_box = SurroundingRectangle(c_comp, color=RED, fill_opacity=0.5)
        l_comp_group = VGroup(l_comp_box, l_comp)

        s_comp = MathTex(r"s(x,y) = \frac{\sigma_{xy} + C_3}{\sigma_x\sigma_y + C_3}", font_size=36, color=WHITE)
        s_comp_box = SurroundingRectangle(s_comp, color=BLUE, fill_opacity=0.5)
        s_comp_group = VGroup(s_comp_box, s_comp)

        c_comp_group.shift(RIGHT*2)
        l_comp_group.next_to(c_comp_group, UP, aligned_edge=LEFT, buff=0.5)
        s_comp_group.next_to(c_comp_group, DOWN, aligned_edge=LEFT, buff=0.5)

        START_POINT += RIGHT*1

        self.play(total_windows.animate.shift(RIGHT*1), WN_label.animate.shift(RIGHT*1),
                  mu_line.animate.put_start_and_end_on(START_POINT, l_comp_box.get_edge_center(LEFT)),
                  sigma_line.animate.put_start_and_end_on(START_POINT, c_comp_box.get_edge_center(LEFT)),
                  covariance_line.animate.put_start_and_end_on(START_POINT, s_comp_box.get_edge_center(LEFT)),
                  Transform(mu_group, l_comp_group), 
                  Transform(sigma_group, c_comp_group), 
                  Transform(covariance_group, s_comp_group))
        self.wait(2)

        tex_1 = MathTex(r"SSIM = [", font_size=36)
        tex_2 = MathTex("l(x,y)", font_size=36, color=RED)
        tex_3 = MathTex(r"]^{\alpha}[", font_size=36)
        tex_4 = MathTex("c(x,y)", font_size=36, color=GREEN)
        tex_5 = MathTex(r"]^{\beta}[", font_size=36)
        tex_6 = MathTex("s(x,y)", font_size=36, color=BLUE)
        tex_7 = MathTex(r"]^{\gamma}", font_size=36)
        ssim = VGroup(tex_1, tex_2, tex_3, tex_4, tex_5, tex_6, tex_7).arrange(RIGHT)
        ssim.shift(RIGHT*2)
        ssim_box = SurroundingRectangle(ssim, color=WHITE, fill_opacity=0)
        ssim_group = VGroup(ssim_box, ssim)
        
        ssim_cond = MathTex(r"where\ (\alpha, \beta, \gamma) > 0", font_size=32, color=YELLOW)
        ssim_cond.move_to(bottom_message)
        
        self.play(FadeOut(mu_group), Transform(sigma_group, ssim_group), FadeOut(covariance_group), Uncreate(bottom_message),
                  mu_line.animate.put_start_and_end_on(START_POINT, ssim_box.get_edge_center(LEFT)),
                  sigma_line.animate.put_start_and_end_on(START_POINT, ssim_box.get_edge_center(LEFT)),
                  covariance_line.animate.put_start_and_end_on(START_POINT, ssim_box.get_edge_center(LEFT)))
        self.play(Write(ssim_cond))
        self.wait(2)

        mssim = MathTex(r"MSSIM(X,Y) = \frac{1}{M}\sum_{j=1}^{M}SSIM(x_j, y_j)", font_size=64)

        self.play(FadeOut(total_windows, WN_label, mu_line, sigma_line, covariance_line, sigma_group, ssim_cond))
        self.play(Write(mssim))
        self.wait(2)

class OverviewOne(Scene):
    def construct(self):
        #formal def
        degredation = MathTex(r"I_x = D(I_y; \delta)", font_size=64).scale(0.8)
        degredation.shift(UP*2.5)

        regeneration = MathTex(r"\hat{I_y} = F(I_x; \theta)", font_size=64).scale(0.8)
        regeneration.shift(UP*1.5)

        formal_def_container = Rectangle(color=WHITE, fill_opacity=0)
        formal_def_container.shift(UP*2)
        formal_def_container_label = Text("formal definition").scale(0.6)
        formal_def_container_label.next_to(formal_def_container, UP, buff=0.1)

        formal_def_group = VGroup(formal_def_container, formal_def_container_label, degredation, regeneration)

        self.play(FadeIn(formal_def_group))
        self.wait()

        #limitations by info theory (data processing inequality)
        DPE = MathTex(r"X \rightarrow Y \rightarrow Z; {I(X;Y) \geq I(X;Z)}", font_size=64).scale(0.8)
        DPE.shift(DOWN*0.5)

        limitations_container = SurroundingRectangle(DPE, color=WHITE, fill_opacity=0)
        limitations_container_label = Text("limitation").scale(0.6)
        limitations_container_label.next_to(limitations_container, UP, buff=0.1)

        limitations_group = VGroup(limitations_container, limitations_container_label, DPE)

        self.play(FadeIn(limitations_group))
        self.wait()

        #quality metrics
        metrics = MathTex(r"MSE, PSNR, MSSIM", font_size=64).scale(0.8)
        metrics.shift(DOWN*2.5)

        metrics_container = SurroundingRectangle(metrics, color=WHITE, fill_opacity=0)
        metrics_container_label = Text("quality metrics").scale(0.6)
        metrics_container_label.next_to(metrics_container, UP, buff=0.1)

        metrics_group = VGroup(metrics_container, metrics_container_label, metrics)

        self.play(FadeIn(metrics_group))
        self.wait(2)

        LR = Square(color=GRAY, fill_opacity=0.5)
        LR.shift(LEFT*3)
        LR_label = Text("Low Res").scale(0.6)
        LR_label.move_to(LR)

        F_mapping = Circle(color=ORANGE, fill_opacity=0.5).scale(0.5)
        F_mapping_label = Text("F", color=WHITE, slant=ITALIC).scale(0.6)

        q_mark = MathTex(r"?", font_size=64)
        q_mark.next_to(F_mapping, UP, buff=0.1)

        HR = Square(color=BLUE, fill_opacity=0.5)
        HR.shift(RIGHT*3)
        HR_label = Text("High Res").scale(0.6)
        HR_label.move_to(HR)

        line_1 = Line(LR.get_edge_center(RIGHT), F_mapping.get_edge_center(LEFT))
        line_2 = Line(F_mapping.get_edge_center(RIGHT), HR.get_edge_center(LEFT))

        self.play(FadeOut(degredation), FadeOut(regeneration), FadeOut(formal_def_container), FadeOut(formal_def_container_label),
                  FadeOut(DPE), FadeOut(limitations_container), FadeOut(limitations_container_label),
                  FadeOut(metrics), FadeOut(metrics_container), FadeOut(metrics_container_label))
        self.play(FadeIn(LR), Write(LR_label), FadeIn(F_mapping), Write(F_mapping_label), FadeIn(HR), Write(HR_label))
        self.play(Create(line_1))
        self.play(Create(line_2))
        self.wait()
        self.play(Write(q_mark))

class ConvNet(ThreeDScene):
    def construct(self):
        #orientation lock
        PHI_OG = 0*DEGREES
        THETA_OG = -90*DEGREES
        GAMMA_OG = 0*DEGREES
        PHI_CONV = -75*DEGREES
        THETA_CONV = 0*DEGREES
        GAMMA_CONV = 90*DEGREES

        input = Square(side_length=4, color=GRAY, fill_opacity=0.5)
        input_label = Text("Input").scale(0.6)
        input_label.move_to(input)
        input_group = VGroup(input, input_label)

        input_R = Square(side_length=4, color=RED, fill_opacity=0.9)
        input_R_label = Text("Input_R").scale(0.6)
        input_R_label.move_to(input_R)
        input_G = Square(side_length=4, color=GREEN, fill_opacity=0.75)
        input_G_label = Text("Input_G").scale(0.6)
        input_G_label.move_to(input_G)
        input_B = Square(side_length=4, color=BLUE, fill_opacity=0.6)
        input_B_label = Text("Input_B").scale(0.6)
        input_B_label.move_to(input_B)

        rgb_group = VGroup(input_B, input_B_label, input_G, input_G_label, input_R, input_R_label)
        rgb_group.shift(IN*4)

        feature_map_R = Square(side_length=2.5, fill_opacity=0.9, color=RED)   
        feature_map_R_label = Text("feature map R").scale(0.6)
        feature_map_G = Square(side_length=2.5, fill_opacity=0.75, color=GREEN)
        feature_map_G.shift(IN*0.2)
        feature_map_G_label = Text("feature map G").scale(0.6)
        feature_map_B = Square(side_length=2.5, fill_opacity=0.6, color=BLUE)
        feature_map_B.shift(IN*0.4)
        feature_map_B_label = Text("feature map B").scale(0.6)

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
        
        self.play(FadeIn(input_group))
        self.move_camera(phi=PHI_CONV, theta=THETA_CONV, gamma=GAMMA_CONV)
        self.play(input_group.animate.shift(IN*4))
        self.play(FadeOut(input_group), FadeIn(rgb_group))
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

        dot_1 = Sphere(radius=0.1)
        dot_2 = dot_1.copy()
        dot_2.shift(OUT*0.4)
        dot_3 = dot_2.copy()
        dot_3.shift(OUT*0.4)

        conv_black_box_R = VGroup(dot_1, dot_2, dot_3)
        conv_black_box_R.shift(OUT)
        conv_black_box_L = conv_black_box_R.copy()
        conv_black_box_L.shift(IN*3.5)

        array_center = MathTex(r"\vdots", font_size=96)
        array_1 = Square(side_length=0.4, fill_opacity=0)
        array_1.next_to(array_center, UP, buff=0.4)
        array_2 = array_1.copy()
        array_2.next_to(array_1, UP, buff=0)
        array_3 = array_1.copy()
        array_3.next_to(array_2, UP, buff=0)
        array_4 = array_1.copy()
        array_4.next_to(array_3, UP, buff=0)
        array_5 = array_1.copy()
        array_5.next_to(array_center, DOWN, buff=0.4)
        array_6 = array_1.copy()
        array_6.next_to(array_5, DOWN, buff=0)
        array_7 = array_1.copy()
        array_7.next_to(array_6, DOWN, buff=0)
        array_8 = array_1.copy()
        array_8.next_to(array_7, DOWN, buff=0)

        array_group = VGroup(array_center, array_1, array_2, array_3, array_4, array_5, array_6, array_6, array_7, array_8)
        array_group.shift(OUT*3)

        self.play(FadeIn(rgb_group), FadeIn(conv_black_box_L), FadeIn(conv_black_box_R), FadeIn(array_group))
        self.play(input_G.animate.shift(OUT*0.2), input_G_label.animate.shift(OUT*0.2),
                  input_B.animate.shift(OUT*0.4), input_B_label.animate.shift(OUT*0.4))
        self.play(FadeOut(rgb_group), FadeIn(input_group))
        self.wait()
        self.play(FadeOut(input_group), FadeOut(conv_black_box_L), FadeOut(feature_map_group), FadeOut(conv_black_box_R), 
                  array_group.animate.shift(IN*3))
        self.move_camera(phi=PHI_OG, theta=THETA_OG, gamma=GAMMA_OG)

        array_label = Text("flattened array of feature maps", color=YELLOW).scale(0.6)
        array_label.next_to(array_group, DOWN, buff=0.5)

        self.play(Write(array_label))
        self.wait()
        self.play(Uncreate(array_label), array_group.animate.shift(LEFT*3))

        NN = Circle(color=ORANGE, fill_opacity=0.5).scale(0.5)
        NN_label = Text("NN").scale(0.8)
        NN_label.move_to(NN)

        HR_output = Square(color=BLUE, fill_opacity=0.5)
        HR_output.shift(RIGHT*3)
        HR_label = Text("HR Output").scale(0.6)
        HR_label.move_to(HR_output)

        array_to_NN = Line(ORIGIN+LEFT*2.5, NN.get_edge_center(LEFT))
        NN_to_output = Line(NN.get_edge_center(RIGHT), HR_output.get_edge_center(LEFT))

        self.play(FadeIn(NN, NN_label))
        self.play(Create(array_to_NN))
        self.play(Create(NN_to_output), FadeIn(HR_output, HR_label))
        self.wait()

class SparseCoding(Scene):
    def construct(self):
        willy = Willy_square.copy().scale(10)

        component_side_length = willy.width / 4

        component_1 = Square(side_length=component_side_length, fill_opacity=0.75, color=BLUE)
        component_1_label = MathTex(r"\varphi_{1}", font_size=32)
        component_1_label.move_to(component_1)
        comp_1 = VGroup(component_1, component_1_label)

        component_2 = component_1.copy()
        component_2_label = MathTex(r"\varphi_{2}", font_size=32)
        component_2_label.move_to(component_2)
        comp_2 = VGroup(component_2, component_2_label)

        comp_skip = MathTex(r"\vdots", font_size=96)

        component_3 = component_1.copy()
        component_3_label = MathTex(r"\varphi_{n-1}", font_size=32)
        component_3_label.move_to(component_3)
        comp_3 = VGroup(component_3, component_3_label)

        component_n = component_1.copy()
        component_n_label = MathTex(r"\varphi_{n}", font_size=32)
        component_n_label.move_to(component_n)
        comp_4 = VGroup(component_n, component_n_label)

        comp_2.next_to(comp_skip, UP, buff=0.4)
        comp_3.next_to(comp_skip, DOWN, buff=0.4)
        comp_1.next_to(comp_2, UP, buff=0)
        comp_4.next_to(comp_3, DOWN, buff=0)
        
        dictionary = VGroup(comp_1, comp_2, comp_skip, comp_3, comp_4)
        dictionary.shift(RIGHT*2)
        
        self.play(FadeIn(willy))
        self.wait()
        self.play(willy.animate.shift(LEFT*2))

        left_brace = Brace(willy, LEFT)
        left_brace.next_to(willy, LEFT)
        right_brace = Brace(willy, RIGHT)
        right_brace.next_to(willy, RIGHT)
        brace_group = VGroup(left_brace, right_brace)

        extraction_arrow = MathTex(r"\rightarrow", font_size=64)
        extraction_arrow.shift(RIGHT)

        self.play(FadeIn(brace_group))
        self.play(FadeIn(extraction_arrow))
        self.play(FadeIn(comp_1))
        self.play(FadeIn(comp_2))
        self.play(Write(comp_skip))
        self.play(FadeIn(comp_3))
        self.play(FadeIn(comp_4))
        self.wait()
        self.play(FadeOut(brace_group), FadeOut(extraction_arrow), FadeOut(dictionary), willy.animate.scale(0.8))

        decomposition = MathTex(r"= \sum_{i=1}^{n}{a_i\varphi_i}", font_size=64)
        decomposition.shift(RIGHT*1.5)

        self.play(Write(decomposition))

class NetworkPlan(Scene):
    def construct(self):
        network = ImageMobject("assets/network.png")

        layer_one_label = Text(r"1. patch extraction", font_size=64)
        layer_two_label = Text(r"2. non-linear mapping", font_size=64)
        layer_two_label.next_to(layer_one_label, DOWN*2, aligned_edge=LEFT)
        layer_three_label = Text(r"3. reconstruction", font_size=64)
        layer_three_label.next_to(layer_two_label, DOWN*2, aligned_edge=LEFT)

        layer_one = MathTex(r"\text{1. } F_1(Y) = max(0, W_1*Y + B_1)", font_size=64)
        layer_two = MathTex(r"\text{2. } F_2(Y) = max(0, W_2*F_1(Y) + B_2)", font_size=64)
        layer_two.next_to(layer_one, DOWN*2, aligned_edge=LEFT)
        layer_three = MathTex(r"\text{3. } F(Y) = W_3*F_2(Y) + B_3", font_size=64)
        layer_three.next_to(layer_two, DOWN*2, aligned_edge=LEFT)

        self.play(FadeIn(network))
        self.wait()
        self.play(network.animate.scale(0.75))
        self.play(network.animate.shift(UP*2))
        self.play(Write(layer_one_label))
        self.wait()
        self.play(Write(layer_two_label))
        self.wait()
        self.play(Write(layer_three_label))
        self.wait()
        self.play(Transform(layer_one_label, layer_one))
        self.wait()
        self.play(Transform(layer_two_label, layer_two))
        self.wait()
        self.play(Transform(layer_three_label, layer_three))
        self.wait()


    