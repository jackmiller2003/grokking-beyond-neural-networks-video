from manim import *


class SummaryOfPaper(Scene):
    def construct(self):
        # Set the background color to black
        self.camera.background_color = BLACK

        # Title for the summary section
        summary_title = Text("Summary of Paper", font_size=36, color=WHITE).to_edge(
            UP, buff=0.5
        )

        # Display the title with an animation
        self.play(Write(summary_title))
        self.wait(1)

        # Bullet points list
        bullet_points = [
            "1. Grokking occurs outside of neural networks",
            "2. Data augmentation induces grokking",
            "3. Explicit regularisation is sometimes required",
        ]

        # Initialize an empty list to keep track of bullet point objects
        bullet_point_objects = []

        for i, point in enumerate(bullet_points):
            # Create a bullet point
            bp_text = Text(point, font_size=24, color=WHITE)

            # If it's the first bullet point, position it relative to the title
            if i == 0:
                bp_text.next_to(summary_title, DOWN, buff=1)
            else:
                # Position subsequent bullet points relative to the previous one
                bp_text.next_to(bullet_point_objects[-1], DOWN, buff=0.5)

            bullet_point_objects.append(bp_text)

            # Animate each bullet point with a pause
            self.play(Write(bp_text))
            self.wait(2)

        # Hold the scene for a moment after displaying all bullet points
        self.wait(2)

        # Fade out all elements
        self.play(FadeOut(summary_title), *[FadeOut(bp) for bp in bullet_point_objects])

        self.wait(1)
