from manim import *

Willy_standard = ImageMobject("assets/Willy-Standard.png").scale(0.1)
Willy_pixelated = ImageMobject("assets/Willy-Pixelated.png").scale(0.1)
Willy_square = ImageMobject("assets/Willy-Square.png").scale(0.1)

class QualityMetrics(Scene):
    def construct(self):  
        mse_tag = Text("1. MSE", font_size=64)
        psnr_tag = Text("2. PSNR", font_size=64)
        ssim_tag = Text("3. SSIM", font_size=64)

        mse_tag.next_to(psnr_tag, UP, buff=0.5, aligned_edge=LEFT)
        ssim_tag.next_to(psnr_tag, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Write(mse_tag))
        self.wait()
        self.play(Write(psnr_tag))
        self.wait()
        self.play(Write(ssim_tag))
        self.wait()

        mse_psnr_group = VGroup(mse_tag, psnr_tag)
        group_box = SurroundingRectangle(mse_psnr_group, color=WHITE, fill_opacity=0)

        self.play(FadeIn(group_box))
        self.wait()
        self.play(FadeOut(mse_tag, psnr_tag, ssim_tag, group_box))

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