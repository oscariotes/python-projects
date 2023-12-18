# The mechanics came from this link https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love


YourName = input('What is your name: ').lower()
OtherName = input('What your match name: ').lower()
combined = YourName+OtherName



t = combined.count('t') 
r = combined.count('r') 
u = combined.count('u') 
e = combined.count('e')
l = combined.count('l')
o = combined.count('o')
v = combined.count('v')


true = (t + r + u + e) * 10 + ( l + o + v + e)



if true < 10 or true > 90:
    print(f'Your score is {str(true)}, you go together like Coke and Mentos')
elif true >= 40 and true <=50:
    print(f'Your score is {str(true)}, you are alright together')
else:
    print(f'Your score of {str(true)} is z')





