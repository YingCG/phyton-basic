# import another_module

# print(another_module.anoter_variable)

# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

newScreen = Screen()
print(newScreen.canvheight)
newScreen.exitonclick()

