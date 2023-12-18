import random

names = input('Please give at least 5 or 6 names: ')

newList = names.split(',')
##number = len(newList)
##anotherList = newList[random.randint(0, number)]

number = newList[random.randint(0, len(newList)-1)]





pick = random.choice(newList)



print(f'The random name is {pick}')
##print(f'Another volunteer is {anotherList}')
print(f'The random name is {number}')
