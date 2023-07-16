# open this file --> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# move the robot

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid(4, 5)
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
root.mainloop()

# def turn_around():
#     turn_left()
#     turn_left()


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# # jump()
# # jump()
# # jump()
# # jump()
# # jump()
# # jump()

# for step in range(6):
#     jump()
