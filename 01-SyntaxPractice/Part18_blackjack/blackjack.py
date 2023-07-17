############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

userHand = []
computerHand = []

def drawOnecard():
    card_on_userhands = random.choice(cards)
    userHand.append(card_on_userhands)
    card_on_computerhands = random.choice(cards)
    computerHand.append(card_on_computerhands)
    

def showAllCards():
    # for card in userHand:
    #     print(card)
    # for card in computerHand:
    #     print(card)
    print(f"Your Cards: {userHand} | Computer Cards: {computerHand}")

def calculateScore(hand):
    sum = 0
    for card in hand:
        if card == "A":
            sum += 11
        elif card == "J" or card == 'Q' or card == 'K':
            sum += 10
        else:
            sum += int(card)
    return sum

def isBlackJack(score):
    return score == 21

def isBusted(score):
    return score > 21


if __name__ == '__main__':
    drawOnecard()
    drawOnecard()
    showAllCards()
    drawCard = (input("Press 'Y' to draw another card, or 'N' to pass"))
    while drawCard == 'y':
        drawOnecard()
        showAllCards()
        userScore = calculateScore(userHand)
        computerScore = calculateScore(computerHand)

        drawCard = (input("Press 'Y' to draw another card, or 'N' to pass"))
