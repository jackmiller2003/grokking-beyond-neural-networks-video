from manim import *
import numpy as np


def create_heatmap(data, num_rows, num_cols, cell_size, colormap, min_value, max_value):
    """
    Create a heatmap from given data.

    Parameters:
    - data: 2D array of data values
    - num_rows, num_cols: Dimensions of the data
    - cell_size: Size of each cell in the heatmap
    - colormap: Manim colormap for coloring the cells based on data value
    - min_value, max_value: Range of data values for normalization

    Returns:
    - heatmap: A VGroup of colored squares representing the heatmap
    """
    grid_width = num_cols * cell_size
    grid_height = num_rows * cell_size
    heatmap = VGroup()
    for i in range(num_rows):
        for j in range(num_cols):
            value = data[i, j]
            color_index = int(
                ((value - min_value) / (max_value - min_value)) * (len(colormap) - 1)
            )
            color = colormap[color_index]
            cell = Square(
                side_length=cell_size, fill_color=color, fill_opacity=1, color=color
            )
            # Adjust y-coordinate for vertical flip (top becomes bottom)
            cell.move_to(
                np.array(
                    [
                        j * cell_size - grid_width / 2 + cell_size / 2,
                        (i - num_rows + 1) * cell_size
                        + grid_height / 2
                        - cell_size / 2,
                        0,
                    ]
                )
            )
            heatmap.add(cell)
    return heatmap


class HeatMapGrid(Scene):
    def construct(self):

        self.camera.background_color = BLACK

        title = Text(
            "Regularisation and GP Grokking",
            font_size=40,
            color=WHITE,
        )

        # Fade in
        self.play(Write(title))

        # Wait for 3 seconds
        self.wait(1)

        # Fade out
        self.play(FadeOut(title))

        num_rows, num_cols = (
            50,
            50,
        )  # 100, 100  # Dimensions based on your actual data size
        cell_size = 0.06  # 0.03  # Cell size for the heatmap

        # Load actual data
        complexity_grid_values = np.load("data/complexity_terms.npy")[::2, ::2]
        datafit_grid_values = np.load("data/fit_terms.npy")[::2, ::2]
        combined_terms = np.load("data/ml.npy")[::2, ::2]

        complexity_min, complexity_max = np.min(complexity_grid_values), np.max(
            complexity_grid_values
        )

        datafit_min, datafit_max = np.min(datafit_grid_values), np.max(
            datafit_grid_values
        )

        combined_min, combined_max = np.min(combined_terms), np.max(combined_terms)

        # Define colormap
        colormap = color_gradient([RED, WHITE, BLUE], 256)

        # Create heatmaps
        complexity_heatmap = create_heatmap(
            complexity_grid_values,
            num_rows,
            num_cols,
            cell_size,
            colormap,
            complexity_min,
            complexity_max,
        )
        datafit_heatmap = create_heatmap(
            datafit_grid_values,
            num_rows,
            num_cols,
            cell_size,
            colormap,
            datafit_min,
            datafit_max,
        )
        ml_heatmap = create_heatmap(
            combined_terms,
            num_rows,
            num_cols,
            cell_size,
            colormap,
            combined_min,
            combined_max,
        )

        # Adjust positions for vertical alignment
        complexity_heatmap.shift(LEFT * num_cols * cell_size)
        datafit_heatmap.next_to(complexity_heatmap, RIGHT, buff=2 * cell_size)
        ml_heatmap.next_to(datafit_heatmap, RIGHT, buff=2 * cell_size)

        centre_of_datafit_heatmap = datafit_heatmap.get_center()

        # Minus datafit centre from all heatmaps
        complexity_heatmap.shift(-centre_of_datafit_heatmap)
        ml_heatmap.shift(-centre_of_datafit_heatmap)
        datafit_heatmap.shift(-centre_of_datafit_heatmap)

        complexity_label = Text("Complexity", font_size=30).next_to(
            complexity_heatmap, UP, buff=0.5
        )

        datafit_label = (
            Text("Data Fit", font_size=30)
            .next_to(datafit_heatmap, UP, buff=0.5)
            .align_to(complexity_label, UP)
        )

        ml_label = Text("Marginal Likelihood", font_size=30).next_to(
            ml_heatmap, UP, buff=0.5
        )

        # Fade in heatmaps from left to right
        self.play(FadeIn(complexity_heatmap), Write(complexity_label), run_time=2)
        self.play(FadeIn(datafit_heatmap), Write(datafit_label), run_time=2)
        self.play(FadeIn(ml_heatmap), Write(ml_label), run_time=2)

        # Hold the scene for a moment
        self.wait(2)

        # Load path data
        ls_paths = np.load("data/ls_paths.npy")  # Example path
        ll_paths = np.load("data/ll_paths.npy")

        # Calculate offsets for path animation based on heatmap dimensions
        x_offset = -num_cols * cell_size / 2 + cell_size / 2
        y_offset = num_rows * cell_size / 2 - cell_size / 2

        # Assuming complexity_heatmap, datafit_heatmap, and ml_heatmap are created as before
        # Position heatmaps
        # Assuming complexity_heatmap, datafit_heatmap, ml_heatmap, and labels are added as before

        grid_height = num_rows * cell_size

        min_x_value, max_x_value = -5, 5
        min_y_value, max_y_value = -7, 4

        all_paths = []
        all_labels = []

        # Animate paths on each heatmap
        for heatmap in [complexity_heatmap, datafit_heatmap, ml_heatmap]:

            centre_of_heatmap = heatmap.get_center()
            print(f"Centre is: {centre_of_heatmap}")

            paths = []

            labels = ["A", "B", "C"]

            for ll_path, ls_path, label in zip(ll_paths, ls_paths, labels):

                path_points = []
                for ll, ls in zip(ll_path, ls_path):
                    epsilon = 0.05

                    ll = ll * (1 - epsilon)
                    ls = ls * (1 - epsilon)

                    # Convert ll and ls to the heatmap's coordinate system
                    # Here we assume ll and ls are already in appropriate log scale
                    x = (ls - min_x_value) / (
                        max_x_value - min_x_value
                    ) * num_cols * cell_size - num_cols * cell_size / 2
                    y = (ll - min_y_value) / (
                        max_y_value - min_y_value
                    ) * num_rows * cell_size - num_rows * cell_size / 2

                    # Adjust for vertical flip of heatmap
                    # y = -y + grid_height / 2 - cell_size / 2

                    # Decrease the value of x and y by a small amount
                    # to ensure the path starts inside the heatmap

                    path_points.append(np.array([x, y, 0]))

                    # Recentre
                    # path_points = [point + centre_of_heatmap for point in path_points]

                # Recenter the path
                path_points = [point + centre_of_heatmap for point in path_points]

                path = VMobject()
                path.set_points_smoothly(path_points)

                paths.append(path)

                # Create a label at the start of the path to indicate the path type

                all_labels.append(
                    Text(label, font_size=24, color=WHITE).next_to(
                        path_points[0], RIGHT, buff=0.1
                    )
                )

            all_paths.extend(paths)

        self.play(
            *[Create(path) for path in all_paths],
            run_time=5,
        )
        self.play(*[Write(label) for label in all_labels], run_time=2)

        # Place a dot at the end of each path

        all_elements = VGroup(
            complexity_heatmap,
            datafit_heatmap,
            ml_heatmap,
            complexity_label,
            datafit_label,
            ml_label,
            *all_paths,
            *all_labels,
        )

        # Hold the scene with all elements shown
        self.wait(2)

        animation = all_elements.animate(run_time=1).scale(0.65).shift(2 * UP)
        self.play(animation)

        # Hold the final scene to view the transformation
        self.wait(2)

        # Draw an arrow from the start of the B path in the marginal likelihood to a box in the centre of the screen
        arrow = Arrow(
            start=all_labels[-5].get_right(),
            end=ORIGIN,
            color=WHITE,
            buff=0.2,
            stroke_width=3,
        )

        # Change starting position of arrow to be up and left a little bit
        arrow.shift(UP * 0.2 + LEFT * 0.3)

        # Create some axes near the centre of the screen
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-0.5, 6, 1],
            x_length=7,
            y_length=4,
            axis_config={"color": WHITE},
        ).scale(0.8)

        # Move axes down
        axes.shift(DOWN * 1.5)

        # Create labels y=mse and x=epochs
        graph_label = axes.get_axis_labels(x_label="Epochs", y_label="MSE")

        graph_label[0].shift(LEFT * 0.5)
        graph_label[0].scale(0.7)
        graph_label[1].scale(0.7)

        # Write sigmoids going from high to low with the training already low and the generalisation decreasing
        sigmoid_1 = axes.plot(
            lambda x: 5 / (1 + np.exp(x + 4)),
            x_range=[0, 10],
            color=BLUE,
        )

        sigmoid_2 = axes.plot(
            lambda x: 5 / (1 + np.exp(2 * x - 10)),
            x_range=[0, 10],
            color=RED,
        )

        # Place an asterix next to the plot with text saying this is not the actual
        # behaviour of the grokking curve but is a simplified version.

        asterix_text = (
            Text("* This is a simplification of the observed curve")
            .scale(0.3)
            .next_to(sigmoid_2, RIGHT, buff=0)
            .shift(LEFT * 0.5)
        )

        # Fade in everything
        self.play(
            Create(arrow),
            Create(axes),
            Write(graph_label),
            Create(sigmoid_1),
            Create(sigmoid_2),
            Write(asterix_text),
        )

        self.wait(2)

        # Fade out
        self.play(
            FadeOut(axes),
            FadeOut(graph_label),
            FadeOut(sigmoid_1),
            FadeOut(sigmoid_2),
            FadeOut(arrow),
            FadeOut(asterix_text),
        )

        self.wait(1)

        hypothesis_title = Text("Hypothesis for Grokking", font_size=28).shift(LEFT * 3)
        dot_point_1 = (
            Text(
                "Low error high complexity solutions are accessible",
                font_size=24,
            )
            .next_to(hypothesis_title, DOWN, aligned_edge=LEFT)
            .shift(RIGHT * 0.5)
        )
        dot_point_2 = Text(
            "Low error low complexity solutions are not accessible", font_size=24
        ).next_to(dot_point_1, DOWN, aligned_edge=LEFT)
        dot_point_3 = Text(
            "Transitioning from high to low complexity improves generalisation",
            font_size=24,
        ).next_to(dot_point_2, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(hypothesis_title))
        self.wait(1)
        self.play(FadeIn(dot_point_1))
        self.wait(1)
        self.play(FadeIn(dot_point_2))
        self.wait(1)
        self.play(FadeIn(dot_point_3))

        self.wait(2)  # Keep the scene displayed for a while

        # Fade everything out
        self.play(
            FadeOut(hypothesis_title),
            FadeOut(dot_point_1),
            FadeOut(dot_point_2),
            FadeOut(dot_point_3),
            *[FadeOut(mob) for mob in all_elements],
        )
