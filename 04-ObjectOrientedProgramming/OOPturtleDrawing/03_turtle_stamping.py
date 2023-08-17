import turtle

#Define program constants
w = 500
h = 500

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Turtle Drawing")
screen.bgcolor("black")

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("cyan")
stamper.shapesize(50 / 20)
stamper.stamp()
stamper.penup()
stamper.shapesize(10 / 20)
stamper.goto(100, 100)
stamper.stamp()

# End the turtle program
turtle.done()
