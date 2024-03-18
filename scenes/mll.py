from manim import *


class MLLScene(Scene):
    def construct(self):

        self.camera.background_color = BLACK

        loss_term = MathTex(r"\mathcal{L}_\text{GP}")
        equals_sign = MathTex("=")
        data_fit_term = MathTex(
            r"-", r"\underbrace{\frac{1}{2} y^T K_\theta^{-1} y}_{\text{data fit}}"
        )
        complexity_term = MathTex(
            r"-", r"\underbrace{\frac{1}{2} \log |K_\theta|}_{\text{complexity}}"
        )
        constant_term = MathTex("+", r"\text{ }C")

        # Position terms next to each other
        equals_sign.next_to(loss_term, RIGHT)
        data_fit_term.next_to(equals_sign, RIGHT).shift(0.3 * DOWN)
        complexity_term.next_to(data_fit_term, RIGHT)
        constant_term.next_to(complexity_term, RIGHT).shift(0.3 * UP)

        # Place everything in a group and centre appropriately
        loss_function = VGroup(
            loss_term, equals_sign, data_fit_term, complexity_term, constant_term
        ).move_to(ORIGIN)

        # Animate each term sequentially
        self.play(Write(loss_term))
        self.play(Write(equals_sign))
        self.play(Write(data_fit_term))
        self.play(Write(complexity_term))
        self.play(Write(constant_term))

        self.wait(1)  # Pause after displaying the loss function

        # Fade out all elements
        self.play(*[FadeOut(mob) for mob in self.mobjects])
