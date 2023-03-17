from random import shuffle

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

mycard = []

for r in RANKS:
    for s in SUITE:
        mycard.append((s, r))


class Deck:
    """
    This object will crete a deck of cards to initiate play. You can use this Deck list of cards to split in half and give to the players.
    It willuse SUITE and RANKS to create the deck.
    It should also have a method for splitting/ cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("New Orderd Deck is ready!")
        self.allcards = mycard

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    """
    Each player has a Hand, and can add or remove card form that hand. THere should be an add and remove card method here.
    """

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    """
    Takes in a name and an instance of a Hand class object.
    The player can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.romove_card()
        print("{} has places: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            # war_cards.append(self.hand.cards.pop())
            war_cards.append(self.hand.remove_card())
        return war_cards

    def still_has_cards(self):
        """
        Return TRUE if play still has cards left
        """
        return len(self.hand.cards) != 0


### GAME PLAY ###
print("Welcome to War, let's begin...")

## create new deck and split it in half:
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

## create both players!
comp = Player("computer", Hand(half1))
