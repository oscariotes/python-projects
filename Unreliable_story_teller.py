#!/usr/bin/env python
# coding: utf-8

# In[44]:


def get_user_input(word_class: str):
    user_input: str = input(f'Enter a {word_class}')
    return user_input

name = get_user_input('name: ')
friend = get_user_input('friend: ')
adjective = get_user_input('adjective: ')
verb = get_user_input('verb: ')
noun = get_user_input('noun: ')
location = get_user_input('location: ')
object1 = get_user_input('object: ')
color = get_user_input('color: ')
animal = get_user_input('animal: ')
plural_noun = get_user_input('plural noun: ')
food = get_user_input('food: ')
music = get_user_input('musical instrument: ')
place = get_user_input('place: ')

story = f"""

One {adjective} day, {name} woke up feeling incredibly {adjective}. 

They decided to {verb} to the {place} to meet their friend {friend}. 

Along the way, they encountered a {noun} wearing a {color} hat.

{name} greeted the {noun} and asked if they wanted to {verb} together to find a {adjective} treasure 

hidden in the {location}. The {noun} eagerly agreed and brought along their trusty {noun}.

As they journeyed, they encountered a {adjective} {animal} playing a {music}. 

Surprised but amused, they {verb} along with the music.

Suddenly, a {adjective} storm rolled in, and they sought shelter in a {noun}. 

Inside, they found a mysterious {object1} that glowed in the {color}. 

Excitedly, they decided to {verb} it to see what would happen.

To their surprise, the {object1} transported them to a {adjective} land filled with {plural_noun}. 

They met a {adjective} wizard who offered them a {noun} that granted wishes.

{name} wished for a {adjective} flying machine, and {name} wished for an endless supply of {food}. 

With their wishes granted, they soared through the sky and feasted on {food} while laughing joyfully.

Eventually, they used the flying machine to return home, carrying memories of their {adjective} adventure forever.




"""

print(story)












# In[ ]:





# In[ ]:




