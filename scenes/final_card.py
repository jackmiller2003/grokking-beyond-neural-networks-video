from manim import *


class FinalScene(Scene):
    def construct(self):

        # Header text
        header_text = Text(
            "Grokking Beyond Neural Networks:",
            font_size=40,
            color=WHITE,
        )

        header_text_continued = Text(
            "An Empirical Exploration with Model Complexity",
            font_size=40,
            color=WHITE,
        )

        # Published
        published = Text(
            "Published in Transactions on Machine Learning Research",
            font_size=26,
            color=WHITE,
        )

        see_description = Text(
            "See the description for the link!",
            font_size=26,
            color=WHITE,
        )

        header_text.shift(1.5 * UP)
        header_text_continued.next_to(header_text, DOWN, buff=0.3)
        published.next_to(header_text_continued, DOWN, buff=0.3)
        see_description.next_to(published, DOWN, buff=0.3)

        # Fade in text
        self.play(Write(header_text))
        self.play(Write(header_text_continued))
        self.wait(0.5)
        self.play(Write(published))
        self.wait(0.5)
        self.play(Write(see_description))

        # Wait for 1 second
        self.wait(1)

        # Fade out everything
        self.play(
            FadeOut(header_text),
            FadeOut(header_text_continued),
            FadeOut(published),
            FadeOut(see_description),
        )
