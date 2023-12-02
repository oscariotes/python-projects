import random

def dice_roll():
    return random.randint(1, 6)

def rolling():
    while True:
        try:
            user_input = int(input('How many rolls?: '))
            if user_input <= 0:
                print('Please enter a positive number.')
            else:
                rolls_list = [dice_roll() for _ in range(user_input)]
                print(*rolls_list)
                print('The sum is', sum(rolls_list))
                break
        except ValueError:
            print('Invalid input. Please enter a number.')
            

rolling()








