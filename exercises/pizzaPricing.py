small = 15
medium = 20
large = 25


peperroni = 2
for_large_peperroni = 3
cheese = 1


def order():
    print('-------------------------------')
    print('-------------------------------')
    print('Welcome to Bros Pizza House!')
    print('-------------------------------')
    print('-------------------------------')
    print('-------------------------------')
    print('-------------------------------')
    size = input('What size of pizza fo you want, S, M, or L: ')
    add_pepperoni = input('Do you want to add pepperoni, Y or N: ')
    extra_cheese = input('Do you want to add extra cheese, Y or N: ')

    total_amount = 0

    if size == "S":
        total_amount += 15
    elif size == 'M':
        total_amount += 20
    elif size == 'L':
        total_amount +=25

    if add_pepperoni == 'Y':
        if size == 'S' and size == 'M':
            total_amount += 2
        else:
            total_amount += 3

    if extra_cheese == 'Y':
        total_amount += 1

    print('-------------------------------')
    print('-------------------------------')
    print('-------------------------------')
    print('-------------------------------')
    print('You final bill is', total_amount)
    


     

            
order()
            
        
            

    

   



