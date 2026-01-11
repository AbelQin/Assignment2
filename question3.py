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

        turtle.left(60)          # inward turn
        draw_edge(length, depth - 1)

        turtle.right(120)        # peak of inward triangle
        draw_edge(length, depth - 1)

        turtle.left(60)          # restore direction
        draw_edge(length, depth - 1)