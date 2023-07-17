### A two-card hand of 21 (an ace plus a ten-value card) is called a "blackjack"

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

 
# # The play goes as follows:

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
def startBlackJack():
    if len(playerHand) < 2:
        firstcard = random.choice(cards)
        playerHand.append(firstcard)
        secondcard = random.choice(cards)
        playerHand.append(secondcard)
        print(f"You cards: {playerHand}")
    if len(computerHand) < 2:
        firstcard = random.choice(cards)
        computerHand.append(firstcard)
        secondcard = random.choice(cards)
        computerHand.append(secondcard)
        return
    
 
def drawOneCard():
    moreCard = random.choice(cards)
    playerHand.append(moreCard)
    print(f"You cards: {playerHand}")
    
def calculateScore():
    playerHand = 0
    computerHand = 0
    for i in playerHand:
        playerHand += i
    for i in computerHand:
        computerHand += i
    print(f"You cards: {playerHand}, total: {playerHand}  |  Computer's Card: {computerHand}, total: {computerHand} ")

# display playerCard after drawing the card
startBlackJack()

# if player want to draw more card  
drawMoreCard = input("Press 'Y' to draw another card, or 'N' to pass")
while drawMoreCard  == 'y' and len(playerHand) < 6: 
    drawOneCard()
    calculateScore()
else:
    calculateScore()


# computer will draw card if the point is not exeed 17

# show both player cards

# compare both player cards, and annouce who is the winner.

