from manim import *
import numpy as np

class GoldenRatio(Scene):
    def construct(self):
        # Define the Golden Ratio
        golden_ratio = (1 + np.sqrt(5)) / 2

        # Create a Text object to display the Golden Ratio
        golden_ratio_text = MathTex(r"\Phi = ", "{:.6f}".format(golden_ratio))
        golden_ratio_text.to_edge(UP)

        # Display the golden ratio
        self.play(Write(golden_ratio_text))

        # Create a list to hold the Fibonacci numbers
        fib = [1, 1]

        # Create a Text object to display the Fibonacci sequence
        fib_text = MathTex("1, 1")
        fib_text.next_to(golden_ratio_text, DOWN)

        # Display the first two Fibonacci numbers
        self.play(Write(fib_text))

        # Generate and display the next 8 Fibonacci numbers
        for i in range(8):
            # Generate the next Fibonacci number
            fib.append(fib[-1] + fib[-2])

            # Update the Fibonacci sequence text
            fib_text_new = MathTex(", ".join(map(str, fib)))
            fib_text_new.next_to(golden_ratio_text, DOWN)

            # Transition to the new Fibonacci sequence text
            self.play(Transform(fib_text, fib_text_new))

            # Calculate the ratio of the latest two Fibonacci numbers
            ratio = fib[-1] / fib[-2]

            # Create a Text object to display the ratio
            ratio_text = MathTex("Ratio = {:.6f}".format(ratio))
            ratio_text.next_to(fib_text, DOWN)

            # Display the ratio
            self.play(Write(ratio_text))

            # Wait for a moment before continuing
            self.wait(0.5)

            # Remove the old ratio text
            self.remove(ratio_text)
        self.wait(2)

class GoldenEquation(Scene):
    def construct(self):
        # Declare the equations
        equation1 = MathTex("1 + \\sqrt{5}", " \\over ", "2")
        equation2 = MathTex("\\frac{a + b}{a}", " = ", "\\frac{a}{b}")
        equation3 = MathTex("\\phi", " = ", "1.6180339887...")
        
        # Align the equations vertically
        equations = VGroup(equation1, equation2, equation3).arrange(DOWN, buff=1)

        # Declare the titles
        title1 = Text("The exact value")
        title2 = Text("The proportional relation")
        title3 = Text("The approximate value")

        # Align the titles with the equations
        titles = VGroup(title1, title2, title3).arrange(DOWN, buff=2.2)
        for title, equation in zip(titles, equations):
            title.next_to(equation, LEFT)

        # Animate the titles and equations
        for title, equation in zip(titles, equations):
            self.play(Write(title), Write(equation))
            self.wait(1)

        # Highlight the approximate value of the Golden Ratio
        self.play(Indicate(equation3[2]), run_time=2)
        self.wait()


class ContinuedRatio(Scene):
    def construct(self):
        depth = 7  # Define the depth of the continued fraction
        fraction = self.create_fraction(depth)

        self.play(Write(fraction))
        self.wait()

    def create_fraction(self, depth):
        if depth == 0:
            return MathTex("1")
        elif depth == 1:  # If we reach the second-to-last level, we add three dots.
            return MathTex("1 + \\cfrac{1}{1 + \\dots}")
        else:
            return MathTex("1 + \\cfrac{1}{" + self.create_fraction(depth - 1).get_tex_string() + "}")


class GoldenRootSquare(Scene):
    def construct(self):
        depth = 7  # Define the depth of the square root sequence
        sqrt_sequence = self.create_sqrt_sequence(depth)

        self.play(Write(sqrt_sequence))
        self.wait()

    def create_sqrt_sequence(self, depth):
        if depth == 0:
            return MathTex("1")
        elif depth == 1:  # If we reach the second-to-last level, we add three dots.
            return MathTex("\\sqrt{1 + \\dots}")
        else:
            return MathTex("\\sqrt{1 + " + self.create_sqrt_sequence(depth - 1).get_tex_string() + "}")


class GoldenSpiral(MovingCameraScene):
    def construct(self):
        # Number of arcs to draw
        num_arcs = 10

        # Initial parameters
        radius = 0.5
        last_endpoint = np.array([radius, 0, 0])

        # We'll keep track of the last arc so we can continue from it
        last_arc = None

        # Define a list of colors
        colors = [RED, BLUE, GREEN, ORANGE, PURPLE, YELLOW, PINK, TEAL]

        # Iterate for each arc we want to draw
        for i in range(num_arcs):
            # Define the arc
            arc_start_angle = i * np.pi / 2
            arc = Arc(start_angle=arc_start_angle, radius=radius, angle=np.pi / 2)
            arc.shift(last_endpoint - arc.get_start())
            arc.set_color(YELLOW)  # Set the color of the arc
            arc.set_z_index(1) # Keep arc above

            # Update the last arc
            last_arc = arc
            last_endpoint = arc.get_end()

            # The radius for the next arc is the current radius times the golden ratio
            radius *= (1 + np.sqrt(5)) / 2

            # Create the square
            start_vertex = arc.get_start()
            end_vertex = arc.get_end()
            length_diag = np.linalg.norm(end_vertex - start_vertex) / np.sqrt(2)
            center = (start_vertex + end_vertex) / 2



            # Create the square as a Polygon
            square = Square(length_diag).move_to(center)
            square.set_color(PINK)  # Set the color of the square

            # create the text
            text = Text(str(i)).set_color(WHITE)
            text.scale_to_fit_width(square.width / 5)
            text.move_to(square.get_center())

            # Move and zoom the camera frame to fit the current display
            self.play(self.camera.frame.animate.set_width(square.width * 3))

            # Draw the square
            self.play(Create(square), run_time=0.5)

            # Draw the text
            self.play(Create(text))

            # Draw the arc
            self.play(Create(arc))


        self.wait()
