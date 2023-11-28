from random import randint

randomNumber= randint(1, 20)
print(randomNumber)

while True:
    try:
      user_input = int(input('Guess the number between 1 to 20: '))
    except ValueError as e:
      print('Please enter a valid number')
    continue
    if user_input > randomNumber:
      print('The number entered is greater than the current value')
    elif user_input < randomNumber:
      print('The number entered is lower than the current value')
    else:
      print('You\n guessed it right!')
    break