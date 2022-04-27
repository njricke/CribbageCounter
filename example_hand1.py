from CribbageCounterClass import *

card1 = Card('5', 'D') #Instance of a Card
card2 = Card('8', 'H')
card3 = Card('6', 'H')
card4 = Card('5', 'H')
flipCard = Card('7', 'D')

hand1 = CribbageHand(card1, card2, card3, card4, flipCard)

print(hand1.count_points())

#Should return 12 points
