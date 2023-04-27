# Step 1 a list of words and list for pictures

# word_list = ['hammock', 'coffee', 'meditation']
import Hangman_art
# front Wordlist import word_list

# Step 2: Randomly choose a word from the word_list and assign it to a variable called chosen_word
import random
chosenword = random.choice(Hangman_art.word_list)
word_length = len(chosenword)

end_of_game = False
lives = 6

print(f'The answer is: {chosenword}')

# # Step 3: Create a placeholder for the chosen word as hint
display = []
for letter in range(word_length):
    display += "_"

# # Step 4: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guessing = input("Guess a letter: ").lower()

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    
    # Step 5: Check if the letter the user guessed (guess) is one of the leters in the chosen_word

    if guess in display:
      print(f"You've already guessed {guess}")
      
    for position in range(len(chosenword)):
        letter = chosenword[position]
        # print(f"Current position: {position} \n Current Letter: {letter} \n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            
    if guess not in chosenword:
        print(f"you guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win")

# Step 6: Display the ascii art according
print(Hangman_art.stages[lives])

