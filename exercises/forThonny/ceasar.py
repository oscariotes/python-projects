alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


text = 'mjqqt'
shift = 5

def newEncrypt(text, shift):
    newText = ''
    for i in text:
        y = alphabeth.index(i)
        z = (y - shift) % len(alphabeth)
        newText += alphabeth[z]
    
    print(newText)

newEncrypt(text, shift)