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
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 10, 10, 10]
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10 , 'J', 'Q', 'K']

# 2 player each hold some card
playerHand = []
computerHand = []

# if player want to draw more card  
def drawMoreCard():
    playing = True
    while playing: 
        moreCard = input("Press 'Y' to draw another card, or 'N' to pass ")
    # if drawMoreCard  == 'y' and len(playerHand) < 6: 
        if moreCard  == 'y':
            card = random.choice(cards)
            playerHand.append(card)
            print(f"You cards: {playerHand}")
        else:
            playing = False
        
    # computer will draw card if the point is not exeed 17    
    while calculateScore(computerHand) < 17:
        card = random.choice(cards)
        computerHand.append(card)
    else:
       pass
    

# each player will have a ramdom drawing of card X two times
def startBlackJack():

    if len(playerHand) < 2:
        card = random.choice(cards)
        playerHand.append(card)
        card = random.choice(cards)
        playerHand.append(card)
        print(f"You cards: {playerHand}")
        
    if len(computerHand) < 2:
        card = random.choice(cards)
        computerHand.append(card)
        card = random.choice(cards)
        computerHand.append(card)
    drawMoreCard()
    playerScore = calculateScore(playerHand)
    computerScore = calculateScore(computerHand)
    print(f"You cards: {playerHand}, total: {playerScore}  |  Computer's Card: {computerHand}, total: {computerScore} ")
    whoIsWinning(playerScore, computerScore)

def calculateScore(hand):
    sum = 0
    aceCounter = 0
    for card in hand:
        if card == "A":
            sum += 11
            aceCounter += 1
        elif card == "J" or card == 'Q' or card == 'K':
            sum += 10
        else:
            sum += int(card)
        
        if sum > 21 and aceCounter > 0:
            sum = sum - 10
            aceCounter = aceCounter - 1
    return sum

def whoIsWinning(playerScore, computerScore):
    blackjack = 21

    # compare both player cards, and annouce who is the winner.
    if calculateScore(playerHand[0:2]) == blackjack:
        print('Player Wins with blackJack')
    elif calculateScore(computerHand[0:2]) == blackjack:
        print('Computer wins with blackJack')
    elif playerScore == 21 and computerScore == 21:
        print('Everybody Win')
    elif playerScore == 21:
        print('You Win')
    elif computerScore == 21:
        print('You lost')
    elif playerScore > 21 and computerScore > 21:
        print('Nobody win')
    elif playerScore > 21 and  computerScore < 21:
        print('You lost')
    elif playerScore <= 21 and computerScore > 21:
        print('You win')
    elif playerScore > computerScore and playerScore <= 21:
        print('You win')
    elif playerScore == computerScore and playerScore < 22:
        print('Everybody Win')
    elif blackjack - playerScore < blackjack - computerScore:
            print('You Win')
    elif blackjack - playerScore > blackjack - computerScore:
            print('You Lost')
        

# display playerCard after drawing the card
startBlackJack()




