# Step 1 - different stage of game & choice of words
import Hangman_art 
hangingStages = Hangman_art.stages

import Wordlist
import random
wordChoice = random.choice(Wordlist.word_list)
print(wordChoice)
print(len(hangingStages))

# Step 2 - display the placeholder for the wordChoice
print(len(wordChoice)) * "_"