import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())




def calculate_score(user_cards, computer_cards):
    blackjack = 0
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    if user_score == 21 or computer_score == 21:
        return blackjack
    if user_score > 21 or computer_score > 21:
        user_cards.remove(11)
        user_cards.append(1)
        computer_cards.remove(11)
        user_cards.append(1)
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)
    else:
        return user_score, computer_score
    
calculate_score(user_cards, computer_cards)