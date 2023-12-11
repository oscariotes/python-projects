from art import logo
print(logo)

alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(textInput, shiftInput, directional):
    
   
    newText = ''
    for i in text:
        if i in alphabeth:
            y = alphabeth.index(i)
            if directional == 'encode':
                z = (y + shift) % len(alphabeth)
            elif directional == 'decode':
                z = (y - shift) % len(alphabeth)
            newText += alphabeth[z]
        else:
            newText += i
    print(f'The {directional}d text is {newText}')
   


while True:
    direction = input('Type \'encode\' to encrypt and \'decode\' to decrypt:\n').lower()
    if direction != 'encode' and direction != 'decode':
        print("Invalid input. Please type 'encode' or 'decode'.")
        continue


    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    caesar(text, shift, direction)

    choice = input('Do you want to go again? Type "yes" to continue or any other key to exit:\n')
    if choice.lower() != 'yes':
        break