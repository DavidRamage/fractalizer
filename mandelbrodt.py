import click
import turtle
@click.command()
@click.option('--iterations','-i',default=100)
def mandelbrodt(iterations):
  # Define the size of the turtle window
  window_size = 600
  
  # Define the range of values to iterate over
  xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
  
  # Define the number of iterations for the Mandelbrot algorithm
  max_iter = iterations
  
  # Define the color palette for the Mandelbrot set
  colors = ["#000000", "#111111", "#222222", "#333333", "#444444", "#555555", "#666666", "#777777", "#888888", "#999999", "#aaaaaa", "#bbbbbb", "#cccccc", "#dddddd", "#eeeeee", "#ffffff"]
  
  # Set up the turtle window
  turtle.setup(window_size, window_size)
  turtle.speed('fastest')
  turtle.title("Mandelbrot Set")
  turtle.bgcolor("#000000")
  
  # Create a turtle object
  t = turtle.Turtle()
  t.hideturtle()
  t.penup()
  t.speed(0)
  
  # Iterate over all the pixels in the turtle window and draw the Mandelbrot set
  for x in range(-window_size//2, window_size//2):
      for y in range(-window_size//2, window_size//2):
          # Calculate the corresponding complex number for the pixel coordinates
          c = complex(x / window_size * (xmax - xmin) + xmin, y / window_size * (ymax - ymin) + ymin)
  
          # Check if the complex number is in the Mandelbrot set
          if is_in_mandelbrot_set(c,max_iter):
              # Calculate the color index based on the number of iterations
              color_index = min(int(max_iter / 16 * abs(c.imag + c.real)), max_iter - 1)
  
              # Set the turtle color and draw the pixel
              t.color(colors[color_index])
              t.goto(x, y)
              t.dot()
  
  # Hide the turtle and keep the turtle window open
  t.hideturtle()
  turtle.mainloop()

# Define the function to check if a complex number is in the Mandelbrot set
def is_in_mandelbrot_set(c,max_iter):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return False
    return True
