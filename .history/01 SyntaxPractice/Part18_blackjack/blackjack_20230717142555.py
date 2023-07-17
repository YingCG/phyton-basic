### A two-card hand of 21 (an ace plus a ten-value card) is called a "blackjack"

# The play goes as follows:

# If the dealer has blackjack and the player doesn't, the player automatically loses.
# If the player has blackjack and the dealer doesn't, the player automatically wins.
# If both the player and dealer have blackjack then it's a push.
# If neither side has blackjack, then each player plays out his hand, one at a time.
# When all the players have finished the dealer plays his hand.

# The player's options for playing his or her hand are:

# Hit: Take another card.
# Stand: Take no more cards.
import random
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10 , 'J', 'Q', 'K']

# 2 player each hold some card
playerHand = []
computerHand = []

# each player will have a ramdom drawing of card X two times
def drawOneCard(hand):
    if len(playerHand) < 2 and len(computerHand) < 2:
        oneCard = random.randint(0,1)
        hand.append(oneCard)
    print(f"player : {playerHand} | computer: {computerHand}")
    

# display call the playerCard

# if player want to draw more card  

# computer will draw card if the point is not exeed 17

# show both player cards

# compare both player cards, and annouce who is the winner.
