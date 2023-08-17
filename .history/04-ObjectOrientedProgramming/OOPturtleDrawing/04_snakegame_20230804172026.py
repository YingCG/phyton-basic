import turtle

w = 500
h = 500
delay = 400

def move_snake():
    stamper.clearstamps()
    new_head = snake[-1].copy()
    new_head[0] += 20
    snake.append(new_head)
    snake.pop(0)
    
    for segment in snake:
        stamper.goto(segment[0], segment[1])
    stamper.stamp()
    
    screen.update()
    turtle.ontimer(move_snake, delay)


screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake Game")
screen.bgcolor('pink')
screen.tracer(0) # turn off automatic animation

stamper = turtle.Turtle()
stamper.shape('square')
stamper.penup()


# create snake as a list of coordinat pairs.
snake = [[0,0], [20, 0], [40, 0], [60, 0]]

# Draw snake for the first time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

move_snake()

turtle.done()