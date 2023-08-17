import turtle


# def square200():
#     turtle.forward(200)
#     turtle.left(-90)
#     turtle.forward(200)
#     turtle.left(-90)
#     turtle.forward(200)
#     turtle.left(-90)
#     turtle.forward(200)
#     turtle.left(-90)


# square200()
side = int(input("What is the legth of each side?"))


def square(side):
    turtle.forward(side)
    turtle.left(-90)
    turtle.forward(side)
    turtle.left(-90)
    turtle.forward(side)
    turtle.left(-90)
    turtle.forward(side)
    turtle.left(-90)


square(side)
