# Step 1 - different stage of game & choice of words
import Hangman_art 
hangingStages = Hangman_art.stages

import random
import Wordlist
end_of_game = False
wordChoice = random.choice(Wordlist.word_list)
wordlist = ['hammock', 'coffee', 'meditation']
# wordChoice = random.choice(wordlist)

print(wordChoice)
print(len(wordChoice))

lives = 6

# Step 2 - display the placeholder for the wordChoice
display = []
for letter in wordChoice:
    # print("_" * len(wordChoice))
    display += '_'
print(display)

# Step 3 - get user input and make it not case sensitive
while not end_of_game:
    playerGuess = input("Guess a letter").lower()

# Step 4 - compare the guess letter in the list, add to display if the letter in the position is correct
for position in range(0, len(wordChoice) -1):
    letter = wordChoice[position]
    if playerGuess == letter:
        display[position] = playerGuess
    
# same as this -->
# position = 0
# for letter in wordChoice:
#     if playerGuess == letter:
#         display[position] = playerGuess
#     position += 1
if playerGuess not in wordChoice:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose")

if "_" not in display:
    end_of_game = True
    print("You win")
         
print(display)

# Step 5 - let the player continue to play while the placeholder is still empty.

    
    