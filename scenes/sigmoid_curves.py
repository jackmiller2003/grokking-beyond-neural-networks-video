from manim import *


class SigmoidCurves(Scene):
    def construct(self):
        # Initial text display
        title_text = Text(
            "Grokking Beyond Neural Networks", font_size=40, color=WHITE
        ).move_to(ORIGIN)

        # Subtitle text, smaller and below the main title
        subtitle_text = Text(
            "by Jack Miller, Charles O'Neill, and Thang Bui", font_size=24, color=WHITE
        ).next_to(title_text, DOWN)

        self.wait(3)

        # Display the texts with an animation
        self.play(Write(title_text))

        self.wait(1)

        self.play(Write(subtitle_text))

        # Fade out the text before proceeding
        self.play(FadeOut(title_text), FadeOut(subtitle_text))

        # Hold the text for a moment
        self.wait(3)

        # Set the background color to black
        self.camera.background_color = BLACK

        # Create axes
        axes = Axes(
            x_range=[-1, 25, 1],
            y_range=[0, 1, 0.1],
            axis_config={"color": WHITE},
            # x_axis_config={"include_numbers": True},
            # y_axis_config={"include_numbers": True},
        )

        # Sigmoid function
        sigmoid = lambda x: 1 / (1 + np.exp(-x))

        # Original sigmoid curve
        # sigmoid_curve = axes.plot(sigmoid, color=BLUE, x_range=[0, 20])

        # Translated sigmoid curve (e.g., horizontally shifted right by 2 units)
        translated_sigmoid_curve_training = axes.plot(
            lambda x: sigmoid(x - 5), color=BLUE, x_range=[0, 25]
        )

        # Translated sigmoid curve (e.g., horizontally shifted right by 2 units)
        translated_sigmoid_curve_gen = axes.plot(
            lambda x: sigmoid(x - 15), color=RED, x_range=[0, 25]
        )

        # Add axes and both curves to the scene
        self.play(
            Create(axes),
        )

        self.wait(0.5)

        # Add labels to the axes
        x_label = axes.get_x_axis_label("Epochs")
        y_label = axes.get_y_axis_label("Accuracy")

        self.play(Create(x_label), Create(y_label))

        # Hold the scene
        self.wait(0.5)

        self.play(Create(translated_sigmoid_curve_training), run_time=1.5)

        # Hold the scene
        # self.wait(0.5)

        self.play(Create(translated_sigmoid_curve_gen), run_time=1.5)

        # Hold the scene
        self.wait(0.5)

        target_y = 0.95
        inv_sigmoid = lambda y, k: np.log((1 / y) - 1) * -1 + k

        x1 = inv_sigmoid(target_y, 5)  # For the first curve (blue)
        x2 = inv_sigmoid(target_y, 15)  # For the second curve (red)

        # Get the y-coordinate in the axes' coordinates
        y_value = axes.c2p(0, target_y)[1]

        # Points on the curves where y = 0.95
        point1 = axes.c2p(x1, target_y)
        point2 = axes.c2p(x2, target_y)

        # Draw a line with arrows at both ends
        connection_line = (
            Line(start=point1, end=point2, color=WHITE)
            .add_tip(tip_length=0.2)
            .add_tip(tip_length=0.2, at_start=True)
        )

        # Add the line to the scene
        self.play(Create(connection_line))

        # Create a label for the line
        delta_k_label = MathTex("\\Delta_k", color=WHITE).next_to(
            connection_line, DOWN, buff=0.1
        )

        # Add the label to the scene
        self.play(Create(delta_k_label))

        # Hold the scene
        self.wait(2)

        # Fade all
        self.play(
            FadeOut(axes),
            FadeOut(translated_sigmoid_curve_training),
            FadeOut(translated_sigmoid_curve_gen),
            FadeOut(connection_line),
            FadeOut(delta_k_label),
        )
