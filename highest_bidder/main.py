import os
from art import logo

print(logo)


info = {}

def bidder(name, bid):
    info[name] =bid
    

while True:
    name = str(input('Please enter your name: ')).upper()
    bid = int(input('Please enter the bid amont $'))
    bidder(name, bid)
    ask = str(input('Is there another bidder? Enter "y" for "yes" or press any other key to end. '))
    if ask == 'y':
        os.system('clear') # Works with mac or linux 
        continue
    else:
        max_value = max(info.values())
        for key, value in info.items():
            if value == max_value:
                highest_key = key
        print(f"The winner is {highest_key} with ${max_value}")
   

""" info = {'bob': 200, 'charlie': 300, 'larry': 100,}

high = 0
winner = " "
for amount in info:
    value = info[amount]
    if value > high:
        high = value
        winner = amount
print(winner, high)       

     """