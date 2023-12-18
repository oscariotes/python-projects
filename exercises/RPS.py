import random


# Rock Paper Scissors ASCII Art

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


art = [Rock, Paper, Scissors]

player_move = int(input('What do you move? Type 0 for Rock, 1 for Paper and 2 for Scissors?\n  '))
computer = [0, 1, 2]

if player_move > 3 or player_move < 0:
    print('invalid number so the computer wins!')

computer_move = random.choice(computer)
print(f'Your move is: {art[player_move]}')

print(f'computer move is {art[computer_move]}:')


if player_move == computer_move:
    print('It\'s a tie!')
elif (player_move == 0  and computer_move == 2) or\
     (player_move == 1  and computer_move == 0) or\
     (player_move == 2  and computer_move == 1):
     print('You win!')
else:
    print('The computer won!') 
 


