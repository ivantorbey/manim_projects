from manim import *
import numpy as np
def fibonacci(n):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    
    if n <= 1:
        return sequence[:n+1]  # Return the sequence up to n (inclusive) if n is 0 or 1
    
    while len(sequence) <= n:
        next_number = sequence[-1] + sequence[-2]  # Calculate the next number in the sequence
        sequence.append(next_number)  # Add the next number to the sequence
        
    return sequence
# Define the Golden Ratio

golden_ratio = (1 + np.sqrt(5)) / 2

class GoldenRatio(Scene):
    def construct(self):

        # Create a Text object to display the Golden Ratio
        golden_ratio_text = MathTex(r"\Phi = ", "{:.6f}".format(golden_ratio))
        golden_ratio_text.to_edge(UP)

        # Display the golden ratio
        self.play(Create(golden_ratio_text))

        # Create a list to hold the Fibonacci numbers
        fib = [1, 1]

        # Create a Text object to display the Fibonacci sequence
        fib_text = MathTex("1, 1")
        fib_text.next_to(golden_ratio_text, DOWN)

        # Display the first two Fibonacci numbers
        self.play(Create(fib_text))

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
            self.play(Create(ratio_text))

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

        title = Text("Golden Spiral", font_size=70)
        title.to_edge(UP)
        title.set_color(GOLD)
        description = Text("Cosmic beauty of the Fibonacci sequence.", font_size=40)
        description.next_to(title, DOWN, buff=1)

        self.play(Write(title), run_time=2)
        self.wait()
        self.play(Write(description), run_time=4)
        self.wait()
        self.play(FadeOut(description,title))

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
            arc = Arc(start_angle=arc_start_angle, radius=radius, angle=np.pi / 2,stroke_width=golden_ratio**i)
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
            square = Square(length_diag,stroke_width=golden_ratio**i).move_to(center)
            square.set_color(PINK)  # Set the color of the square

            # create the text
            
            text = Text(str(fibonacci(i+3)[-1])).set_color(WHITE)
            text.scale_to_fit_width(square.width / 7)
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




class GoldenFraction(Scene):
    def construct(self):

        title = Text("Golden Fraction", font_size=70)
        title.to_edge(UP)
        title.set_color(GOLD)
        description = Text("How beautiful the golden ratio is", font_size=40)
        description.next_to(title, DOWN, buff=1)

        self.play(Write(title), run_time=2)
        self.wait()
        self.play(Write(description), run_time=4)
        self.wait()
        self.play(FadeOut(description,title))

        a = 2.0
        b = a / ((1 + np.sqrt(5)) / 2) # compute b using the golden ratio formula

        # Shifting segments upwards
        a_segment = Line(ORIGIN+(a+b)*LEFT/2 + 8*UP,  8*UP+(b-a)*LEFT/2, color=YELLOW)
        b_segment = Line(a * RIGHT+(a+b)*LEFT/2 + 8*UP, 8*UP+(a+b)*RIGHT/2, color=BLUE)
        a_plus_b_segment = Line(ORIGIN+(a+b)*LEFT/2 + 8*UP, 8*UP+(a+b)*RIGHT/2, color=GREEN)

        a_label = MathTex("a").next_to(a_segment, DOWN)
        b_label = MathTex("b").next_to(b_segment, DOWN)
        a_plus_b_label = MathTex("a + b").next_to(a_plus_b_segment, UP)

        self.play(Write(a_plus_b_segment), Write(a_plus_b_label))
        self.wait()

        self.play(Write(a_segment), Write(a_label))
        self.wait()

        self.play(Write(b_segment), Write(b_label))
        self.wait()

        # Moving Golden Ratio equation to middle of screen
        golden_ratio_eqn = MathTex("\\frac{a}{b} = \\frac{a + b}{a}")
        golden_ratio_eqn.next_to(a_plus_b_label,DOWN*5)
        
        self.play(Write(golden_ratio_eqn))
        self.wait()
        golden_ratio_eqn2 = MathTex(r"\Phi = "+"\\frac{a}{b}")
        golden_ratio_eqn2.next_to(golden_ratio_eqn,DOWN*3)
        self.play(Write(golden_ratio_eqn2))
        golden_ratio_eqn3 = MathTex("\\frac{a}{b} = 1+\\frac{b}{a}")
        golden_ratio_eqn3.next_to(a_plus_b_label,DOWN*5)
        self.play(Transform(golden_ratio_eqn, golden_ratio_eqn3))
        golden_ratio_eqn4=MathTex(r"\Phi ="+" 1+\\frac{1}{"+r"\Phi"+"}")
        golden_ratio_eqn4.next_to(golden_ratio_eqn,DOWN*3)
        self.play(Transform(golden_ratio_eqn2, golden_ratio_eqn4))

        phi_expression = "\\phi"
        phi_term = MathTex(phi_expression).scale(1.5).next_to(golden_ratio_eqn4,5*DOWN+5*LEFT)
        self.play(Write(phi_term))
        self.wait()

        equal_sign = MathTex("=").scale(1.5).next_to(phi_term)
        self.play(Write(equal_sign))
        self.wait()

        start_expression = "\\phi"
        start_term = MathTex(start_expression).scale(1.5).next_to(equal_sign)
        self.play(Write(start_term))
        self.wait()

        for _ in range(8):
            start_expression = "1 + \\frac{1}{" + start_expression + "}"
            next_term = MathTex(start_expression).next_to(equal_sign)
            self.play(Transform(start_term, next_term))
            self.wait()

        approx = MathTex("\\approx 1.618").scale(1.5).next_to(start_term, DOWN)
        self.play(Write(approx))
        self.wait()
