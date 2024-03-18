from manim import *


class GrokkingScene(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Title that says "Grokking Occurs Beyond Neural Networks"
        title = Text(
            "Grokking Occurs Beyond Neural Networks", font_size=40, color=WHITE
        )

        # Fade in
        self.play(Write(title))

        # Wait for 3 seconds
        self.wait(1)

        # Fade out
        self.play(FadeOut(title))

        # GP Box, Polynomial Curve, and Dots
        gp_box = Rectangle(
            width=4, height=3, color=WHITE
        )  # Change border color to white
        gp_text = Text("GP", color=WHITE, font_size=24).next_to(gp_box, UP, buff=0.1)
        self.play(Create(gp_box), Write(gp_text))

        # Polynomial curve and data points
        polynomial_curve = FunctionGraph(
            lambda x: 0.15 * x**3 - 0.05 * x**2 + 0.05 * x,
            x_range=[-2, 2],
            color=GREEN,
        ).move_to(gp_box.get_center())

        polynomial_curve.set_z_index(-1)

        # Add dots one at a time with color white
        for j, x in enumerate(np.linspace(-1.5, 1.5, 5)):
            dot = Dot(
                point=polynomial_curve.point_from_proportion(
                    (x + 2 + 0.1 * np.random.randn()) / 4
                ),
                color=WHITE,  # Change dot color to white
            )

            # Offset dot by noise
            if j != 0 and j != 4:
                dot.shift(0, 0.15 * np.random.randn(), 0)

            self.play(Create(dot), run_time=0.2)  # Add Create animation for each dot

        self.play(Create(polynomial_curve))

        # Drawing the brackets for the vector more accurately
        bracket_height = 3.5
        bracket_width = 0.5
        left_bracket_start = gp_box.get_left() + LEFT * 3 + UP * bracket_height / 2
        left_bracket_end = left_bracket_start + DOWN * bracket_height
        right_bracket_start = left_bracket_start + RIGHT * bracket_width
        right_bracket_end = left_bracket_end + RIGHT * bracket_width

        # Left Bracket
        self.play(
            Create(Line(left_bracket_start, left_bracket_end, color=WHITE))
        )  # Added color=WHITE
        # Right Bracket
        self.play(
            Create(Line(right_bracket_start, right_bracket_end, color=WHITE))
        )  # Added color=WHITE

        # Bits
        bits = ["0", "1", "0", "0", "1", "\\vdots", "0", "1"]

        i = 0

        for bit in bits:
            if i == 3:
                # Wait 1 second
                self.wait(1)

            if bit == "\\vdots":
                i += 1

                position = (
                    left_bracket_start
                    + DOWN * ((i + 1) * 0.3)
                    + RIGHT * (bracket_width / 2)
                )

                bit_text = MathTex(bit, color=WHITE).move_to(position)

                i += 2
            else:
                position = (
                    left_bracket_start
                    + DOWN * ((i + 1) * 0.3)
                    + RIGHT * (bracket_width / 2)
                )
                bit_text = Text(bit, color=WHITE, font_size=24).move_to(position)
                i += 1
            self.play(Write(bit_text), run_time=0.5)

        # Arrow adjustments
        arrow_start = (
            right_bracket_end + RIGHT * bracket_width * 0.5 + UP * bracket_height / 2
        )
        arrow_to_gp = Arrow(
            start=arrow_start,
            end=gp_box.get_left(),
            buff=0.1,
            color=WHITE,
            max_tip_length_to_length_ratio=0.1,  # Make arrow tip smaller
        )
        self.play(Create(arrow_to_gp))

        # Arrow from GP to output
        arrow_from_gp = Arrow(
            start=gp_box.get_right(),
            end=gp_box.get_right() + RIGHT * 2,
            buff=0.1,
            color=WHITE,
            max_tip_length_to_length_ratio=0.1,  # Make arrow tip smaller
        )
        output_text = Text("1", color=WHITE, font_size=36).next_to(
            arrow_from_gp, RIGHT, buff=0.1
        )
        self.play(Create(arrow_from_gp), Write(output_text))

        self.wait(2)

        # Fade everything out at the end
        self.play(*[FadeOut(mob) for mob in self.mobjects])
