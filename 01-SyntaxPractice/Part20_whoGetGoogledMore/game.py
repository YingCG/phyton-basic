# About the game:  What gets Googled more?

from art import logo, vs
from game_data import data
import random

# Display art
print(logo)
score = 0
game_should_continue = True
player2 = random.choice(data)

# Make the game repeatable.
while game_should_continue:

    def format_data(player):
        player_name = player["name"]
        player_desc = player["description"]
        player_country = player["country"]
        return f"{player_name}, {player_desc}, from {player_country}"

    # Generate a random account from the game data.
    # Making account a position B become the next account at position A.

    player1 = player2
    player2 = random.choice(data)
    if player1 == player2:
        player2 = random.choice(data)

    print(f"Compare Player: {format_data(player1)}")
    print(vs)
    print(f"Compare Player: {format_data(player2)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()


    # Check if user is correct.
    ## Get follower count of each account.
    player1_count = player1["follower_count"]
    player2_count = player2["follower_count"]

    ## Check if user is correct.
    def check_answer(guess, player1, player2):
        if player1 > player2:
            # if guess == 'a':
            #     return True
            # else:
            #     return False
            return guess == 'a'
        else:
            return guess == 'b'
        
    is_correct = check_answer(guess, player1_count, player2_count)

    # Clear the screen between rounds.
    clear()


    # Give user feedback on their guess
    # Score keeping.
    if is_correct:
        score += 1
        print('You are right! Current score: {score}')
    else:
        game_should_continue = False
        print("Sorry, that is wrong.")





