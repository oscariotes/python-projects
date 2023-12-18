import random
import os
from artwork import logo

def guess():
    print(logo)
    print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')

    numbers = random.randint(1, 100)
    level = str(input('Choose a difficulty. Type "easy" or "hard": ')).lower()

    def difficulty(level):
        if level == 'easy':
            return 10
        elif level == 'hard':
            return 5
    
    attempt = difficulty(level=level)
    game_over = False
    while True:
        try:
            user_input = int(input('Guess the number: '))
        except ValueError as e:
            print('Please enter a valid number')
            continue
        if user_input > numbers:
            attempt -= 1
            print('The number entered is greater than the current value')
        elif user_input < numbers:
            attempt -= 1
            print('The number entered is lower than the current value')
        else:
            print('You\n guessed it right!')
            break

        if attempt == 0:
            print(f'You\'ve run out of guesses, you lose! The number was {numbers}')
            game_over = True
            break
        print(f'You have {attempt} attempts remaining to guess the number')

guess()

ask = str(input('Do you want to play again? "y" or "n": ')).lower()
if ask == 'y':
    os.system('clear')
    guess()
else:
    exit()