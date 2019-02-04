from enum import Enum
import random
import copy

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.face.name, self.suit.name)

    def __eq__(self, other):
        return self.face == other.face and self.suit == other.suit

class Suit(Enum):
    Spades = 1
    Hearts = 2
    Clubs = 3
    Diamonds = 4

class Face(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


def print_card(card):
    print(card[1], "of", card[0].name)

def compare_card_suit(card, other_card):
    return card[0] == other_card[0]


four_of_spades = (Suit.Spades, "4")
queen_of_hearts = (Suit.Hearts, "Queen")
jack_of_spades = (Suit.Spades, "Jack")
print_card(four_of_spades)
print_card(queen_of_hearts)

print(compare_card_suit(four_of_spades, queen_of_hearts))
print(compare_card_suit(four_of_spades, jack_of_spades))

deck = []

for suit in Suit:
    for face in Face:
        deck.append(Card(face, suit))


#for card in deck:
    #print(card)

random_card = deck[random.randint(0, len(deck)-1)]
print(random_card)

other_deck = copy.deepcopy(deck)

print(deck[0])
print(other_deck[0])

deck[0].face = Face.Ace

print(deck[0])
print(other_deck[0])

first_card = deck[0]

second_card = first_card