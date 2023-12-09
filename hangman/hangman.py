import random

word_list = ['ardvard', 'baboon', 'camel']

choosen_word = random.choice(word_list) # Randomly choose word from word list and assign it to variable choosen_word.abs
print(choosen_word)

display = ['_']* len(choosen_word)
print(display)




while '_' in display:
    
    guess = input('Guess the letter: ').lower()
    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess
            
    print(display)

    if '_' not in display:
        print('You guess all the letters!')





