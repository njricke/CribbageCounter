class Card:
    def __init__(self, number,suit):
        self.name = [number + suit]
        self.suit = str(suit)
        acceptedSuits = ['S', 'C', 'D', 'H']
        acceptedNumbers = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        if self.suit not in acceptedSuits:
            print('Error- Invalid card entered: Not an accepted suit')
            exit()


        cardNumber = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
        }

        cardValue = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10,
        }

        try:
            self.number = cardNumber[str(number)]
            self.value = cardValue[str(number)]
        except:
            print('Error- Invalid card entered: Not an accepted card value')
            exit()
