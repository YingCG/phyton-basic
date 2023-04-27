# Step 1 a list of words and list for pictures
word_list = ['hammock', 'coffee', 'meditation']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Step 2: Randomly choose a word from the word_list and assign it to a variable called chosen_word
import random
chosenword = random.choice(word_list)
print(f'The answer is: {chosenword}')

# # Step 3: Create a placeholder for the chosen word as hint
# display = []
# for letter in range(len(chosenword)):
#     display += "_"
# print(display)

# # Step 4: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guessing = input("Guess a letter: ").lower()

# # for letter in chosenword:
# #     if letter == guessing:
# #         print("Match")
# #     else:
# #         print("Wrong")
# for position in range(len(chosenword)):
#     letter = chosenword[position] 
#     if letter == guessing:
#         display[position] = letter

# Step 5: Check if the letter the user guessed (guess) is one of the leters in the chosen_word
# print(display)

end_of_game = False
display = []
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    
    for position in range(len(chosenword)):
        letter = chosenword[position]
        if letter == guess:
            display[position] = letter
        
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win")
    else:
        print(stages[0])

