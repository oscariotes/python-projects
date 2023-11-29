#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def dice_roll():
    roll = random.randint(1,6)
    return roll

def rolling():
  
  while True:
    try: 
        user_input = int(input('How many rolls?: '))
        if user_input <= 0:
            print('Please enter non-zero number.')
        
        else:
            rolls_list = []
        
            for _ in range(user_input):
                value = dice_roll()  
                rolls_list.append(value)
            
            print(*rolls_list)
            print('the sum is ',sum(rolls_list))
            break
    except ValueError:
        print('Invalid number')
            

rolling()


# In[ ]:




