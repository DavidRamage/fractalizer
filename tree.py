import turtle
import random
import click

@click.command()
@click.option('--iterations','-i',default=8)
def tree(iterations):
  print(iterations)
  # Set up the turtle
  t = turtle.Turtle()
  t.hideturtle()
  t.speed('fastest')
  
  # Define the colors for the branches

  
  # Define the recursive function to draw the tree
  
  
  # Set the starting position and orientation
  t.left(90)
  t.penup()
  t.goto(0, -200)
  t.pendown()
  
  # Draw the tree
  draw_tree(150, 30, iterations, t)
  
  # Hide the turtle and keep the window open
  t.hideturtle()
  turtle.mainloop()

def draw_tree(length, angle, depth, t):
  # Base case: stop recursion when depth = 0
  colors = ['brown', 'sienna', 'saddle brown']
  if depth == 0:
      return

  # Draw the trunk
  t.color('brown')
  t.pensize(depth)
  t.forward(length)

  # Draw the branches
  for i in range(2):
    t.color(random.choice(colors))
    t.pensize(depth-1)
    t.left(angle)
    draw_tree(length*0.7, angle*0.8, depth-1,t)
    t.right(angle*2)
    draw_tree(length*0.7, angle*0.8, depth-1,t)
    t.left(angle)

  # Move back to the starting position
  t.penup()
  t.backward(length)
  t.pendown()
