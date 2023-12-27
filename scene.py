from manim import *

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


