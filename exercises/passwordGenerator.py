import random

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print('**********************************')
print('**********************************')
print('Welcome to the Password Generator')
print('**********************************')
print('**********************************')



lower = int(input('How many lowercase letters?:\n '))
upper = int(input('How many uppercase letters?:\n '))
symbolS = int(input('How many symbols?:\n '))
numberS = int(input('How many numbers?:\n '))


selected_uppercase =[]
for letters in range(upper):
    random.shuffle(uppercase)
    selected_uppercase.append(uppercase[letters])

upcase = ''.join(selected_uppercase)


selected_lowercase = []
for letters in range(lower):
    random.shuffle(lowercase)
    selected_lowercase.append(lowercase[letters])

lowcase = ''.join(selected_lowercase)  


selected_symbols = []
for letters in range(symbolS):
    random.shuffle(symbols)
    selected_symbols.append(symbols[letters])

symb = ''.join(selected_symbols) 

selected_numbers =[]
for number in range(numberS):
    random.shuffle(numbers)
    selected_numbers.append(numbers[number])

numb = ''.join(selected_numbers)



combined = upcase + lowcase + symb + numb #combines generated strings
newCombine = list(combined)
random.shuffle(newCombine) # shuffle strings
password = ''.join(newCombine)
print(combined)
print('**********************************')
print('**********************************')
print(f'Your new password is {password}')
print('**********************************')
print('**********************************')





