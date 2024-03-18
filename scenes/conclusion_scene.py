from manim import *


class ConclusionScene(Scene):
    def construct(self):

        # Header text
        header_text = Text("Conclusion", font_size=40, color=WHITE)

        # Fade in text
        self.play(Write(header_text))

        # Wait for 1 second
        self.wait(1)

        # Fade out text
        self.play(FadeOut(header_text))

        regularisation_question = Text(
            "How does grokking occur without explicit regularisation?",
            font_size=36,
            color=WHITE,
        )

        regularisation_question.shift(1 * UP)

        loss_eq = MathTex(
            r"\mathcal{L}",
            "=",
            r"\text{data fit}",
            "+",
            r"\text{regularisation}",
        )

        # Put loss eq under the question
        loss_eq.next_to(regularisation_question, DOWN, buff=0.5)

        # Put a straight line through regularisation
        reg_line = Line(loss_eq[4].get_left(), loss_eq[4].get_right())

        # Fade in question
        self.play(Write(regularisation_question))
        self.play(Write(loss_eq))
        self.play(Create(reg_line))

        # Wait for 1 second

        self.wait(1)

        # Fade out question and loss equation
        self.play(FadeOut(regularisation_question), FadeOut(loss_eq), FadeOut(reg_line))

        # Next question
        next_question = Text(
            "Thoeretical justifcation for concealment?",
            font_size=36,
            color=WHITE,
        )

        next_question.shift(1 * UP)

        # Correct solutions become less accessible in higher dimensions?
        further_question = Text(
            "Solutions become less accessible in higher dimensions?",
            font_size=30,
            color=WHITE,
        )

        # Place below next question
        further_question.next_to(next_question, DOWN, buff=0.5)

        # Fade in question
        self.play(Write(next_question))
        self.play(Write(further_question))

        # Wait for 1 second
        self.wait(1)

        # Fade out question

        self.play(FadeOut(next_question), FadeOut(further_question))
