""" Title: The Quest for the Enchanted Amulet

Once upon a time in the mystical land of Eldoria, there existed a fabled artifact known as the Enchanted Amulet, said to grant its possessor unimaginable powers. Many brave souls had attempted to retrieve it, but none had succeeded. One day, a young adventurer named Aiden set out on a quest to find the amulet and bring peace to the realm.

Aiden stood at the entrance of the Forest of Whispers, a dense and eerie woodland rumored to hold the amulet deep within its heart. The forest was filled with unknown dangers, and Aiden had to make careful decisions to navigate through it.

As Aiden ventured deeper into the forest, a fork in the path appeared. Two routes lay ahead: one leading through the dark and misty Grove of Shadows, while the other wound its way along the Sunlit Trail.

Facing this choice, Aiden considered the available options:

    Grove of Shadows: Aiden, feeling stealthy, chose to traverse the dark and mysterious Grove of Shadows, hoping to evade any lurking dangers.
    Sunlit Trail: Aiden, preferring a more straightforward path, opted for the Sunlit Trail, seeking safety in the open and bright surroundings.

With resolve, Aiden made the choice to take the Sunlit Trail. The path was serene, illuminated by warm sunlight filtering through the leaves. However, as Aiden walked, a band of mischievous forest imps appeared, blocking the way forward.

Now, Aiden had to decide how to handle the situation:

    Negotiate: Aiden attempted to reason with the imps, hoping to convince them to let him pass peacefully.
    Fight: Aiden readied his sword and prepared to engage the imps in combat.

Aiden chose to negotiate with the imps, using words instead of force. Surprisingly, the imps were swayed by Aiden's sincerity, allowing him to pass without a fight. Beyond them, the path opened up to reveal a hidden grove where the Enchanted Amulet shimmered atop an ancient pedestal.

With the amulet in hand, Aiden felt its mystical power coursing through him. The realm of Eldoria would now know peace, thanks to Aiden's courage and wisdom in making the right choices along the way.

And so, Aiden returned home as a hero, celebrated for his bravery and the wise decisions he made during his quest for the Enchanted Amulet.

The end. """
print('*********************************************')
print('*********************************************')
print('*********************************************')
print('The Quest for the Enchanted Amulet')
print('*********************************************')
print('*********************************************')
print('*********************************************')
print('*********************************************')
print('Once upon a time in the mystical land of Eldoria, \n there existed a fabled artifact known as the Enchanted Amulet,\n said to grant its possessor unimaginable powers. \n Many brave souls had attempted to retrieve it, \n but none had succeeded. One day, a young adventurer named Aiden \n set out on a quest to \n find the amulet and bring peace to the realm. ')
print('')
print('Aiden stood at the entrance of the Forest of Whispers, \n a dense and eerie woodland rumored to hold the amulet deep within its heart. \n The forest was filled with unknown dangers, \n and Aiden had to make careful decisions to navigate through it.')
print('')
print('As Aiden ventured deeper into the forest, \n a fork in the path appeared. Two routes lay ahead: \n one leading through the dark and misty Grove of Shadows, \n while the other wound its way along the Sunlit Trail.')
print('')
print('Facing this choice, Aiden considered the available options:')
print('')
print('You have two choices, on your left the Groove of shadows and on your right The Sunlit trail')
print('')
left = 'left'
right = 'right'
move = input('Are you going to the left or right? ')
if move == left:
    print('Aiden, feeling stealthy, chose to traverse the dark and mysterious Grove of Shadows, hoping to evade any lurking dangers.')
    print('Unfortunately, bad things do happen which left our hero dead!')
elif move == right:
    print('Aiden, preferring a more straightforward path, opted for the Sunlit Trail, seeking safety in the open and bright surroundings.')
    print('With resolve, Aiden made the choice to take the Sunlit Trail. \n The path was serene, illuminated by warm sunlight filtering through the leaves. \n However, as Aiden walked, a band of mischievous \n forest imps appeared, blocking the way forward.')
    print('')
    print('Now, Aiden had to decide how to handle the situation:')
    fight = 'fight'
    negotiate = 'negotiate'
    handle = input('Are you going to negotiate or fight? ')
    if handle == fight:
        print('Aiden readied his sword and prepared to engage the imps in combat.') 
        print('With all his might, the enemies are too many and overwhelmed our hero to the death!!!')
    elif handle == negotiate:
        print('Aiden chose to negotiate with the imps, using words instead of force.\n Surprisingly, the imps were swayed by Aiden\'s sincerity, \n allowing him to go without a fight. \n Beyond them, the path opened up to reveal a hidden grove \n where the Enchanted Amulet shimmered atop an ancient pedestal.')
        print('With the amulet in hand, Aiden felt its mystical power coursing through him.\n The realm of Eldoria would now know peace, thanks to Aiden\'s \n courage and wisdom in making the right choices along the way.')
        print('And so, Aiden returned home as a hero, celebrated for his bravery and \n the wise decisions he made during his quest for the Enchanted Amulet.')
        print('The End')
    else: 
        print('You are now in the abyss! There \'s no mortal or god can save you now!!!')
else:
    print('You are now in the abyss! There \'s no mortal or god can save you now!!!')