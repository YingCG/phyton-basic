rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_images = [rock, paper, scissors]



def playgame():
    yourChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))
    if (yourChoice >= 3 or yourChoice < 0):
        print("Your typed an invalid number, you lose!")
    else:
        print(game_images[yourChoice])
    computerChoice = random.randint(0,2)
    print (f"Computer choose: ")
    print(game_images[computerChoice])

    # compare
    if (yourChoice == 0 ) and (computerChoice == 1):
        print("You lose")
    elif (yourChoice == 0) and (computerChoice == 2):
        print("You win")
    elif (yourChoice == 1) and (computerChoice == 2):
        print("You lose")
    elif (yourChoice == 1) and (computerChoice == 0):
        print("You win")
    elif (yourChoice == 2) and (computerChoice == 0):
        print("You lose")
    elif yourChoice == computerChoice:
        print("It's a Tie")
    else:
        print("You lose")

playgame()