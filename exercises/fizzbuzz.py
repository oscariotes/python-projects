""" Players take turns counting up from 1, replacing numbers that are multiples of 3 with the word "Fizz" and multiples of 5 with the word "Buzz." 
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz."

For example:

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, 
Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, ...

The game continues with each player stating the next number in the sequence, 
substituting the appropriate words for numbers that meet the criteria. If a player hesitates or makes a mistake, they are eliminated from the game. """

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else: 
        print(number)