from manim import *


class TwoImagesFadeIn(Scene):
    def construct(self):
        # Load the images
        image1 = ImageMobject("data/480px-3B1B_Logo.png")
        image2 = ImageMobject("./data/0032083297_10.jpg")

        # Set the height of the images if you want them to be of the same height
        image1.height = 3
        image2.height = 3

        # Position the images side by side, centered horizontally at the origin
        image1.move_to(LEFT * 2)
        image2.move_to(RIGHT * 2)

        # Fade in the images
        self.play(FadeIn(image1), FadeIn(image2))

        # Keep the images displayed for a while before fading out if desired
        self.wait(2)

        # Fade out
        self.play(FadeOut(image1), FadeOut(image2))
