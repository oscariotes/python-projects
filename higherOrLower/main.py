import random
from gameData import data
from artwork import logo, vs

def get_random_data():
    return random.choice(data)

def game():
    print(logo)
    score = 0
    first_data = get_random_data()
    second_data = get_random_data()

    while first_data == second_data:
        second_data = get_random_data()

    while True:
        print(f'{first_data["name"]} is {first_data["description"]} has ___ followers from {first_data["country"]}')
        print(vs)
        print(f'{second_data["name"]} is {second_data["description"]} has ___ followers from {second_data["country"]}')

        user_choice = input('Which has the higher number of followers? Type "A" or "B": ').lower()

        if user_choice == 'a' or user_choice == 'b':
            if (user_choice == 'a' and first_data['follower_count'] > second_data['follower_count']) or \
               (user_choice == 'b' and second_data['follower_count'] > first_data['follower_count']):
                score += 1
                print('Correct!')
                print(f'Your current score is: {score}')
                # Keep the last correct choice for the next comparison
                first_data = second_data  # This will retain the last choice
                second_data = get_random_data()
                while first_data == second_data:
                    second_data = get_random_data()
            else:
                print('Incorrect! Game Over')
                break
        else:
            print('Please enter a valid option (A or B)')

game()

while True:
    continueGame = str(input('Do you want to play another game? y or n '))
    if continueGame == 'y':
        game()
    else:
        print('Thanks for playing!')
        break
     




















