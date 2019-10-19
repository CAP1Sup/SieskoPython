import turtle

wn = turtle.Screen()
wn.bgcolor("red")      # Set the window background color
wn.title("Yeet")      # Set the window title

snake = turtle.Turtle()
snake.color("black")            # Tell tess to change her color
snake.pensize(10)               # Tell tess to set her pen width

snake.forward(100)
snake.left(60)
snake.forward(60)

wn.mainloop()