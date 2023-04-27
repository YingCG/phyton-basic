# Step 1 a list of words and list for pictures
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
word_list = ['hammock', 'coffee', 'meditation']

# Step 2: Randomly choose a word from the word_list and assign it to a variable called chosen_word
import random
chosenword = random.choice(word_list)
word_length = len(chosenword)


print(f'The answer is: {chosenword}')

# # Step 3: Create a placeholder for the chosen word as hint
display = []
for letter in range(word_length):
    display += "_"
print(display)

# # Step 4: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guessing = input("Guess a letter: ").lower()

end_of_game = False
lives = 6

display = []
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    
    # Step 5: Check if the letter the user guessed (guess) is one of the leters in the chosen_word

    for position in range(len(chosenword)):
        letter = chosenword[position]
        print(f"Current position: {position} \n Current Letter: {letter} \n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    print(display)
    
    if guess not in chosenword:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    
    print(f"{''.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win")

