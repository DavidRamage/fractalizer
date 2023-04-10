import turtle
import click
@click.command()
def julia():
    # Set up the turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed('fastest')

    # Define the function to calculate the Julia Set

    # Set the dimensions of the drawing window
    width, height = 800, 800
    turtle.setup(width, height)

    # Set the range of values for the x and y coordinates
    x_range = [-2, 2]
    y_range = [-2, 2]

    # Set the number of pixels in each direction
    pixels_x = width / (x_range[1] - x_range[0])
    pixels_y = height / (y_range[1] - y_range[0])

    # Set the value of c for the Julia Set
    c = complex(-0.7, 0.27)

    # Loop through all the pixels in the window
    for i in range(width):
        for j in range(height):
            # Calculate the x and y coordinates for this pixel
            x = x_range[0] + i / pixels_x
            y = y_range[0] + j / pixels_y
      
            # Calculate whether this pixel is in the Julia Set
            if julia_set(x, y, c):
                t.penup()
                t.goto(i - width / 2, height / 2 - j)
                t.pendown()
                t.dot(1)

    # Hide the turtle and keep the window open
    t.hideturtle()
    turtle.mainloop()

def julia_set(x, y, c):
    z = complex(x, y)
    for i in range(100):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True
