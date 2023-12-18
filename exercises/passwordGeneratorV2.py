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

password = []
for element in range(1, lower + 1):
    password.append(lowercase[element])

for element in range(1, upper + 1):
    password.append(uppercase[element])


for element in range(1, symbolS + 1):
    password.append(symbols[element])

for element in range(1, numberS + 1):
    password.append(numbers[element])

random.shuffle(password)
print(password)
newpass = ''.join(password)
print(newpass)

