#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint

randomNumber = randint(1, 10)
guess_counter = 5
print('Guess the number in five attempts!')

while guess_counter > 0:  # Loop while guess_counter is greater than 0
    try:
        user_input = int(input('Guess the number: '))
    except ValueError as e:
        print('Please enter a valid number')
        continue  # Continue the loop after an invalid input

    if user_input > randomNumber:
        guess_counter -= 1
        print(f'The number {user_input} is greater and you have {guess_counter} tries remaining')
    elif user_input < randomNumber:
        guess_counter -= 1
        print(f'The number {user_input} is lower and you have {guess_counter} tries remaining')
    else:
        print(f'You\'ve guessed it right, the number is {randomNumber}!')
        break  # Exit the loop if the guess is correct

if guess_counter == 0:
    print(f'You failed the attempts. The number was {randomNumber}.')


# In[ ]:




