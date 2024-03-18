from manim import *


class ConcealmentEffectOnGrokking(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Title that says "Grokking Occurs Beyond Neural Networks"
        title = Text(
            "Grokking is Induced via Concealment",
            font_size=40,
            color=WHITE,
        )

        # Fade in
        self.play(Write(title))

        # Wait for 3 seconds
        self.wait(1)

        # Fade out
        self.play(FadeOut(title))

        # Initial vector setup, moved further to the left
        task_vector = VGroup(
            *[
                Square(side_length=0.5, fill_color=WHITE, fill_opacity=1, color=WHITE)
                for _ in range(5)
            ]
        )
        task_vector.arrange(RIGHT, buff=0.1).to_edge(UP, buff=1).shift(
            LEFT * 2
        )  # Shifted left
        task_label = (
            Text("Original Task", font_size=24, color=WHITE)
            .next_to(task_vector, UP, buff=0.1)
            .align_to(task_vector, LEFT)  # Ensuring alignment
        )

        self.play(Create(task_vector), Write(task_label))

        # Initial concealment setup, aligned with task vector horizontally
        concealment_boxes = VGroup()
        for _ in range(2):
            concealment_boxes.add(
                Square(side_length=0.5, fill_color=RED, fill_opacity=1, color=RED)
            )
        concealment_boxes.arrange(RIGHT, buff=0.1).next_to(task_vector, RIGHT, buff=0.5)
        concealment_label = (
            Text("Concealment Strategy", font_size=24, color=RED)
            .next_to(concealment_boxes, UP, buff=0.1)
            .align_to(
                concealment_boxes, LEFT
            )  # Aligning to task label for horizontal alignment
        )

        self.play(Create(concealment_boxes), Write(concealment_label))

        # Adjusting the position of the axes to avoid overlap
        axes = Axes(
            x_range=[0, 30, 5],
            y_range=[0, 60, 10],
            x_length=8,
            y_length=5,
            axis_config={"color": WHITE},
        ).to_edge(DOWN, buff=1)

        graph_label = axes.get_axis_labels(x_label="Epochs", y_label="Accuracy")

        # Move epochs to the left
        graph_label[0].shift(LEFT * 0.5)
        graph_label[1].shift(DOWN * 0.5)

        # Make both labels smaller
        graph_label[0].scale(0.8)
        graph_label[1].scale(0.8)

        self.play(Create(axes), Write(graph_label))

        sigmoid_1 = axes.plot(
            lambda x: 50 / (1 + np.exp(-0.5 * (x - 3))),
            x_range=[0, 30],
            color=BLUE,
        )
        sigmoid_2 = axes.plot(
            lambda x: 50 / (1 + np.exp(-0.5 * (x - 10))),
            x_range=[0, 30],
            color=RED,
        )

        self.wait(1)

        self.play(Create(sigmoid_1), Create(sigmoid_2))

        self.wait(1)

        # Animating concealment boxes addition and grokking curve adjustments simultaneously
        for i in range(3, 7):
            new_box = Square(
                side_length=0.5, fill_color=RED, fill_opacity=1, color=RED
            ).next_to(concealment_boxes, RIGHT, buff=0.1)
            concealment_boxes.add(new_box)

            new_translation_1 = 3 + (i - 2) * 0.2
            new_translation_2 = 10 + (i - 2) * 1.5
            new_sigmoid_1 = axes.plot(
                lambda x: 50 / (1 + np.exp(-0.5 * (x - new_translation_1))),
                x_range=[0, 30],
                color=BLUE,
            )
            new_sigmoid_2 = axes.plot(
                lambda x: 50 / (1 + np.exp(-0.5 * (x - new_translation_2))),
                x_range=[0, 30],
                color=RED,
            )

            self.play(
                Transform(sigmoid_1, new_sigmoid_1),
                Transform(sigmoid_2, new_sigmoid_2),
                FadeIn(new_box),
                run_time=1,
            )

        self.wait(1)

        # Optional fade out
        # self.play(FadeOut(VGroup(*self.mobjects)))

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
