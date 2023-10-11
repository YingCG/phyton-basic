import turtle

#Define program constants
w = 500
h = 500
delay = 20 #milliseconds between screen updatees

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Turtle Drawing")
screen.bgcolor("black")
screen.tracer(0) # Turn off automatic animation

def move_turtle():
    circle_turtle.forward(1)
    circle_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, delay)
    
circle_turtle = turtle.Turtle()
circle_turtle.shape('turtle')
circle_turtle.color('yellow')

# Set animation in motion
move_turtle()

# End the turtle program
turtle.done()
