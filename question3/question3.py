import turtle

# ---------------- Recursive Edge Function ----------------
def draw_edge(length, depth):
    """
    Draws a modified edge using recursion.
    Each recursion replaces a line segment with
    four smaller segments creating an inward indentation.
    """
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3

        draw_edge(length, depth - 1)

        turtle.right(60)          # inward turn
        draw_edge(length, depth - 1)

        turtle.left(120)        # peak of inward triangle
        draw_edge(length, depth - 1)

        turtle.right(60)          # restore direction
        draw_edge(length, depth - 1)
        
        # ---------------- Draw Polygon ----------------
def draw_polygon(sides, length, depth):
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(360/sides)
        # ---------------- Main Program ----------------
def main():
    # User input
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Turtle setup
    turtle.setup(900, 900)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(False)

    # Position turtle nicely
    turtle.penup()
    turtle.goto(-length / 2, length / 2)
    turtle.setheading(0)
    turtle.pendown()

    # Draw pattern
    draw_polygon(sides, length, depth)

    turtle.tracer(True)
    turtle.done()


# Run program
main()