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
        

        self.add(mse)


