import random
from artwork import hangman
from word_file import word_list


print('Save the man from the noose!')


choosen_word = random.choice(word_list) 


display = ['_']* len(choosen_word)
print(*display)



lives = 6
hangman.reverse()

while '_' in display:
    
    guess = input('Guess the letter: ').lower()

    if guess in display:
        print(f'You already guessed the letter {guess}')
    
    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess
    
            
    

    if '_' not in display:
        print('You guessed all the letters!')
        break

    elif guess not in choosen_word:
        lives -= 1
        print(hangman[lives])
        print(f'The letter {guess} is not in the word.')
        if lives <= 0:
            print('You lose!')
            print(f'The correct word is {choosen_word}.')
            break

    print(*display)
      
    


