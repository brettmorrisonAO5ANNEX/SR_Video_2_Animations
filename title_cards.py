from manim import *

class DefiningTheProblem(Scene):
    def construct(self):
        Title = Text("Defining The Problem", font_size=64)

        self.play(Write(Title))
        self.wait()
        self.play(FadeOut(Title))

class CNN(Scene):
    def construct(self):
        Title = Text("CNNs (Briefly) Explained", font_size=64)

        self.play(Write(Title))
        self.wait()
        self.play(FadeOut(Title))

class Connecting(Scene):
    def construct(self):
        Title = Text("Connecting Ideas / Pot. Solutions", font_size=64)

        self.play(Write(Title))
        self.wait()
        self.play(FadeOut(Title))

class Conclusion(Scene):
    def construct(self):
        Title = Text("Conclusion", font_size=64)

        self.play(Write(Title))
        self.wait()
        self.play(FadeOut(Title))