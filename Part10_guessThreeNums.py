# The computer will think of 3 digit number that has no repeating digits.
# User will guess a 3 digit number
# Computer will give clues, base on thse clues you will guess again until the code is match
## Clue to user: 
## Close: if correct number but wrong position
## Match: correct number in correct position
## Nope: nothing is match


######

# generate the code
import random

def start_guess():
    return int(input("What is your guess?"))

# generate the code
def generate_code():
    digits = [num for num in range(10)]

    # Shuffle the digits
    random.shuffle(digits)

    # Then grab the first three
    return digits[:3]


# generate the clues
def give_clues(code, user_guess):

    if user_guess == code:
        return "code cracked!"
    
    clues = []

    # below same as 
    # i = 0
    # i = i++

    for i, num in enumerate(user_guess):
        if num == code[i]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    
    if clues == []:
        return ["Nope"]
    
# run the game logic
print("Welcome code breaker! Let's see if you can guess the 3 digit number!")

secret_code = generate_code()
print(secret_code)

clue_report = []

while "code cracked!" not in clue_report:
    guess = start_guess()

    clue_report = give_clues(guess, secret_code)
    print("here is the result of your guess: ")

    for clue in clue_report:
        print(clue)
        