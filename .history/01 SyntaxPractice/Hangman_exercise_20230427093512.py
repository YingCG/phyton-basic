# Step 1 a list of words
word_list = ['hammock', 'coffee', 'meditation']

# Todo 1: Randomly choose a word from the word_list and assign it to a variable called chosen_word
import random
chosenword = random.choice(word_list)
# placeholder = len(chosenword) + "_"

# Todo 2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guessing = input("Guess a letter: ").lower()

for letter in chosenword:
    if letter == guessing:
        print("Match")
    else:
        print("Wrong")

# Todo 3: Check if the letter the user guessed (guess) is one of the leters in the chosen_word
