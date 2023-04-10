import turtle
import click
@click.command()
@click.option('--iterations','-i',default=3)
def koch(iterations):
    turtle.speed('fastest')
    # adjust size as desired
    size = 300
    # move to starting position
    turtle.penup()
    turtle.goto(-size/2, size/4)
    turtle.pendown()
    # draw Koch snowflake
    for i in range(iterations):
        koch_snowflake(size, 4)
        turtle.right(120)
    turtle.done()

def koch_snowflake(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(length / 3, depth - 1)
            turtle.left(angle)
