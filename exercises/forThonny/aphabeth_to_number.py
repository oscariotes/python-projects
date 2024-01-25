def alphabet_position(text):

    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = []
    for letter in text.lower():
        if letter in alpha:
            result.append(str(alpha.find(letter) + 1))
    return " ".join(result)  



print(alphabet_position("The sunset sets at twelve o' clock."))