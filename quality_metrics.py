from manim import *

Willy_standard = ImageMobject("assets/Willy-Standard.png").scale(0.1)
Willy_pixelated = ImageMobject("assets/Willy-Pixelated.png").scale(0.1)
Willy_square = ImageMobject("assets/Willy-Square.png").scale(0.1)

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

        sigma = MathTex(r"\sigma_x, \sigma_y", font_size=64, color=GREEN)
        sigma.shift(RIGHT*2)
        sigma_box = SurroundingRectangle(sigma, color=GREEN, fill_opacity=0.5)
        sigma_box.move_to(sigma)
        sigma_group = VGroup(sigma, sigma_box)

        mu = MathTex(r"\mu_x, \mu_y", font_size=64, color=RED)
        mu.next_to(sigma, UP, aligned_edge=LEFT, buff=0.5)
        mu_box = SurroundingRectangle(mu, color=RED, fill_opacity=0.5)
        mu_box.move_to(mu)
        mu_group = VGroup(mu, mu_box)

        covariance = MathTex(r"\sigma_{xy}", font_size=64, color=BLUE)
        covariance.next_to(sigma, DOWN, aligned_edge=LEFT, buff=0.5)
        covariance_box = SurroundingRectangle(covariance, color=BLUE, fill_opacity=0.5)
        covariance_box.move_to(covariance)
        covariance_group = VGroup(covariance, covariance_box)

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

        contrast = MathTex(r"\sigma_{\{x,y\}} = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(\{x,y\}_i - \mu_{\{x,y\}})^2}", font_size=36, color=GREEN)
        contrast_box = SurroundingRectangle(contrast, color=GREEN, fill_opacity=0.5)
        contrast_group = VGroup(contrast, contrast_box)

        luminance = MathTex(r"\mu_{\{x,y\}} = \frac{1}{N}\sum_{i=1}^N\{x,y\}_i", font_size=36, color=RED)
        luminance_box = SurroundingRectangle(luminance, color=RED, fill_opacity=0.5)
        luminance_group = VGroup(luminance, luminance_box)
        
        sigma_xy = MathTex(r"\sigma_{xy} = \frac{1}{N-1}\sum_{i=1}^{N}(x_i - \mu_i)(y_i - \mu_y)", font_size=36, color=BLUE)
        sigma_box = SurroundingRectangle(sigma_xy, color=BLUE, fill_opacity=0.5)
        sigma_group = VGroup(sigma_xy, sigma_box)

        contrast_group.shift(RIGHT*3)
        luminance_group.next_to(contrast_group, UP, aligned_edge=LEFT, buff=0.5)
        sigma_group.next_to(contrast_group, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(FadeIn(luminance_group), FadeIn(contrast_group), FadeIn(sigma_group))
        

        #self.play(total_windows.animate.shift(LEFT*1.2), 
        #          mu_line.animate.put_start_and_end_on(START_POINT, ),
         #         sigma_line.animate.put_start_and_end_on(START_POINT, ),
         #         covariance_line.animate.put_start_and_end_on(START_POINT, ))




        """
        c_comp = MathTex(r"c(x,y) = \frac{2\sigma_x\sigma_y + C_2}{{\sigma_x}^2 + {\sigma_y}^2 + C_2}", font_size=36, color=GREEN)
        #shift right here if necessary
        c_comp.shift(RIGHT*1.5)
        
        l_comp = MathTex(r"l(x,y) = \frac{2\mu_x\mu_y + C_1}{{\mu_x}^2 + {\mu_y}^2 + C_1}", font_size=36, color=RED)
        l_comp.next_to(c_comp, UP*4.2, aligned_edge=LEFT)
        
        s_comp = MathTex(r"s(x,y) = \frac{\sigma_{xy} + C_3}{\sigma_x\sigma_y + C_3}", font_size=36, color=BLUE)
        s_comp.next_to(c_comp, DOWN*4.2, aligned_edge=LEFT)

        tex_1 = MathTex(r"SSIM = [", font_size=36)
        tex_2 = MathTex("l(x,y)", font_size=36, color=RED)
        tex_3 = MathTex(r"]^{\alpha}[", font_size=36)
        tex_4 = MathTex("c(x,y)", font_size=36, color=GREEN)
        tex_5 = MathTex(r"]^{\beta}[", font_size=36)
        tex_6 = MathTex("s(x,y)", font_size=36, color=BLUE)
        tex_7 = MathTex(r"]^{\gamma}", font_size=36)
        ssim = VGroup(tex_1, tex_2, tex_3, tex_4, tex_5, tex_6, tex_7).arrange(RIGHT)
        ssim.shift(RIGHT*2.7)
        
        ssim_cond = MathTex(r"where\ (\alpha, \beta, \gamma) > 0", font_size=32, color=YELLOW)
        ssim_cond.move_to(bottom_message)

        mssim = MathTex(r"MSSIM(X,Y) = \frac{1}{M}\sum_{j=1}^{M}SSIM(x_j, y_j)", font_size=64)

        
        self.play(total_windows.animate.shift(LEFT*1.2), WN_label.animate.shift(LEFT*1.2),
                  mu_line.animate.put_start_and_end_on(WN.get_edge_center(RIGHT) + LEFT*1.2, luminance.get_edge_center(LEFT)),
                  sigma_line.animate.put_start_and_end_on(WN.get_edge_center(RIGHT) + LEFT*1.2, contrast.get_edge_center(LEFT)),
                  covariance_line.animate.put_start_and_end_on(WN.get_edge_center(RIGHT) + LEFT*1.2, sigma_xy.get_edge_center(LEFT)),
                  Transform(mu, luminance), Transform(sigma, contrast), Transform(covariance, sigma_xy))
        self.wait(2)
        self.play(Transform(mu, l_comp), Transform(sigma, c_comp), Transform(covariance, s_comp))
        self.wait(2)
        self.play(Uncreate(mu), Transform(sigma, ssim), Uncreate(covariance), Uncreate(bottom_message),
                  sigma_line.animate.put_start_and_end_on(WN.get_edge_center(RIGHT) + LEFT*1.2, ssim.get_edge_center(LEFT)),
                  FadeOut(mu_line), FadeOut(covariance_line))
        self.play(Write(ssim_cond))
        self.wait(2)
        self.play(Uncreate(ssim_cond), FadeOut(total_windows), FadeOut(WN_label), FadeOut(sigma_line), Transform(sigma, mssim))
        self.wait(2)
        """