import random

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },

]

def get_random_data():
    return random.choice(data)

def game():

    x = get_random_data()
    y = get_random_data()

    first = list(x.values())
    second = list(y.values())

 


    

    while True:  # Game loop
        
        x = y
        y = get_random_data()
        second = list(y.values())

        while x == y:
            game = True
            y = get_random_data()
            second = list(y.values())

            print(f'{first[0]} {first[1]} is a {first[2]} from {first[3]}')
            print('VS')
            print(f'{second[0]} {second[1]} is a {second[2]} from {second[3]}')

            chooseAB = input('What is the higher value? Type "A" or "B": ').lower()

            
            def choose():
                
                if chooseAB == 'a' or chooseAB == 'b':
                    if first[1] > second[1]:
                        return first[1]
                    elif second[1] > first[1]:
                        return second[1]
                
                else:
                    print('Please enter a valid option')

            result = choose()

            def gameLoop():
                count = 0
                
                if result == first[1] or result == second[1]:
                    count += 1
                    print(count)
                    print(f'You Win! the highest value')
                else:
                    print(f'You Lose! not the highest value')
                    game = False 

                
            
            gameLoop()

game()