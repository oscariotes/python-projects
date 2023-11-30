import random
import sys

class rps:
    def __init__(self):
        print('Welcome to Rock, Paper, Scissors')

        self.moves = {'rock': '\U0001F91F', 'paper': '\U0001F91F', 'scissors': '\U0001FAA8'}
        self.valid_moves = self.moves.keys()

    def game(self):
        print('------------------------------------------------')

        while True:
            self.player_move = input('Choose your move: ').lower()
            if self.player_move not in self.valid_moves:
                print('Incorrect move, please check your input!')
                print('The valid moves are: rock, paper, scissors')
            else:
                break
                
            

            self.computer_move = random.choice(list(self.valid_moves))

            if self.player_move == 'exit':
                print('Goodbye!')
                sys.exit()

        print('------------------------------------------------')

    def show_moves(self):
        print(f'Your move: {self.moves[self.player_move]}')
        print(f'Computer\'s move: {self.moves[self.computer_move]}')

    def move_check(self):
        player_score = 0
        computer_score = 0

        while player_score < 3 and computer_score < 3:
            self.game()
            self.show_moves()

            if self.player_move == self.computer_move:
                print('It\'s a tie!')
            elif (self.player_move == 'rock' and self.computer_move == 'scissors') or \
                 (self.player_move == 'scissors' and self.computer_move == 'paper') or \
                 (self.player_move == 'paper' and self.computer_move == 'rock'):
                print('You win this round!')
                player_score += 1
            else:
                print('Computer wins this round!')
                computer_score += 1

        if player_score == 3:
            print('------------------------------------------------')
            print('You win the match!')
            print('------------------------------------------------')
        elif computer_score == 3:
            print('------------------------------------------------')
            print('Computer wins the match!')
            print('------------------------------------------------')

if __name__ == '__main__':
    while True:
        game = rps()
        game.move_check()
           

    