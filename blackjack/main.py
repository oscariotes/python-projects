import random
import os
from artwork import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def calculate_score(card_list):
    """Calculates the score based on the card list."""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0  # Blackjack
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def compare(user_score, computer_score):
    """Compares the user and computer scores."""
    if user_score > 21:
        return "You went over. You lose!"
    if computer_score > 21:
        return "The computer went over. You win!"
    if user_score == computer_score:
        return "It's a draw!"
    if user_score == 0:
        return "Blackjack! You win!"
    if computer_score == 0:
        return "Blackjack! The computer wins!"
    if user_score > computer_score:
        return "You win!"
    return "The computer wins!"

def play_game():
    print(logo)
    print("Welcome to Blackjack!")
    user_cards = []
    computer_cards = []

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f'Your cards: {user_cards}, current score: {user_score}')
    print(f"Computer's first card: {computer_cards[0]}")

    while user_score != 0 and user_score < 21:
        draw_card = input('Type "y" to get another card, type "n" to pass: ')
        if draw_card == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f'Your cards: {user_cards}, current score: {user_score}')
        else:
            break

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Your final hand: {user_cards}, final score: {user_score}')
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

def blackjack():
    play_game()
    while input('Do you want to play another game of Blackjack? Type "y" or "n": ') == 'y':
        os.system('clear')
        play_game()
    else:
        exit()

blackjack()
