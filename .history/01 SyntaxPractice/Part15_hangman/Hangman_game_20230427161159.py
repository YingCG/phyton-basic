# Step 1 - different stage of game & choice of words
import Hangman_art 
hangingStages = Hangman_art.stages

import random
# import Wordlist
# wordChoice = random.choice(Wordlist.word_list)
wordlist = ['hammock', 'coffee', 'meditation']
wordChoice = random.choice(wordlist)

print(wordChoice)
print(len(hangingStages))

# Step 2 - display the placeholder for the wordChoice
display = []
for letter in wordChoice:
    # print("_" * len(wordChoice))
    display += '_'
print(display)