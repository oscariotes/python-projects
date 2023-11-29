#!/usr/bin/env python
# coding: utf-8

# ## Word Jumble Game:
# 
# ### Objective: Create a word jumble game where the player unscrambles a randomly chosen word.
# 
#    #### Steps:
#        - Create a list of words.
#        - Randomly select a word from the list.
#        - Scramble the letters of the word to create a jumbled version.
#        - Display the jumbled word to the player.
#        - Prompt the player to unscramble the word.
#        - Validate the guess:
#             - If the guess matches the original word:
#                - Congratulate the player for unscrambling the word.
#             - If the guess is incorrect:
#                 - Allow the player to try again.
#                 - Display a hint (optional) if the player struggles.
#                 
#         - Continue until the player correctly unscrambles the word or decides to quit.
#         
#  ##### Hints for Implementation:
#     
#        - Create a function to scramble the letters of a word.
#        - Display the scrambled word and ask the player to unscramble it.
#        - Use string manipulation methods (like shuffling characters) to create the jumbled word.
#        - Provide hints if the player struggles to unscramble the word.

# In[ ]:


import random

words = ['recover','society','assault','captain','freight','revenge','address','enlarge','release','arrange']


randomWords = random.choice(words)
lis = list(randomWords)
random.shuffle(lis)
newlis = ''.join(lis)

def guess():

    tries = 4
    
    while tries > 0:
        guessedWord = input(f'Guess the word "{newlis}"')
        if guessedWord == randomWords:
            print('You get it right!')
            break
        else:
            tries -= 1
            if tries > 0:
                print(f'Please try again You have {tries} remaining')
            else:
                print(f'Sorry it\s over, the correct word is {randomWords}.')

    
            
guess()
        






# In[ ]:




