from manim import *


class LossFunctionScene(Scene):
    def construct(self):

        self.camera.background_color = BLACK

        title = Text(
            "Loss Functions and Grokking",
            font_size=40,
            color=WHITE,
        )

        # Fade in
        self.play(Write(title))

        # Wait for 3 seconds
        self.wait(1)

        # Fade out
        self.play(FadeOut(title))

        # Display the loss function with explicit parts
        loss_eq = MathTex(
            r"\mathcal{L}", "=", r"\text{data fit}", "+", r"\text{regularisation}"
        )

        loss_eq.shift(1 * UP)

        self.play(Write(loss_eq))
        self.wait(1)  # Pause after displaying the loss function

        # Highlight the data fit term
        data_fit_box = SurroundingRectangle(loss_eq[2], color=BLUE, buff=0.1)
        self.play(Create(data_fit_box))
        self.wait(1)  # Pause after highlighting the data fit term

        # Highlight the regularisation term
        reg_box = SurroundingRectangle(loss_eq[4], color=RED, buff=0.1)
        self.play(ReplacementTransform(data_fit_box, reg_box))
        self.wait(1)  # Pause after highlighting the regularisation term

        # Point down from regularisation
        reg_arrow = Arrow(
            loss_eq[4].get_bottom(),
            loss_eq[4].get_bottom() + 0.75 * DOWN,
            buff=0.1,
            stroke_width=10,
        )

        # Set arrow color to be red
        reg_arrow.set_color(RED)

        # Then set that to be 0
        zero_text = MathTex("0").next_to(reg_arrow, DOWN, buff=0.1)

        # Set 0 text color to be red
        zero_text.set_color(RED)

        self.play(Create(reg_arrow), Write(zero_text))

        self.wait(1)  # Pause after pointing down from regularisation

        # Fade out all elements
        self.play(*[FadeOut(mob) for mob in self.mobjects])
