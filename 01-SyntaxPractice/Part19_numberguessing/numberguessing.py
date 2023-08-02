#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import title
import random

print(title)
levelChoice = ['easy', 'medium', 'hard']
level = int(input("prease '1' for easy, prese '2' for medium, press '3' for hard"))
luckynumber = random.randint(0, 11)
guessnumber = int(input("What is the number you are guessing "))


def guesstheluckynumber(guessnumber):
    guessCount = 3
    if guessnumber < luckynumber:
        message = str(guessnumber)+ " is Too low"
    elif guessnumber > luckynumber:
        message = str(guessnumber) + " is Too High"
    else:
        message = "Bingo! The lucky number indeed is " + str(luckynumber)
    guessCount -= 1
    print(message)

guesstheluckynumber(guessnumber)
