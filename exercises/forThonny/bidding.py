info = {'bob': 200, 'charlie': 300, 'larry': 100,}

high = 0
winner = " "
for amount in info:
    value = info[amount]
    if value > high:
        high = value
        winner = amount
print(winner, high)       

    

    