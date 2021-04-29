import random
def create_deck():
    deck = []
    suits = ["hearts","spades", "diamonds", "clubs"]
    while len(deck) < 40:
        for suit in suits:
            for i in range(1,11):
                card = str(i) + suit
                if card not in deck:
                    deck.append(card)
    print(deck)
    
create_deck()