# Check exercise
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
import random

def move():
    print("go forward")

def turn_left():
    print("turn left")

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


steps = 0
goal = random.randint(1,10)
def at_goal():
    print ("flag here", steps)
    return goal == steps

# while at_goal() != True:
#     jump()
#     steps += 1

# # same as above, but simplify:
while not at_goal():
    jump()
    steps += 1
    print(steps)


## with a random wall
wall = random.randint(1,6)
currentStep = 0

def wall_in_front():
    if steps != wall:
        move()