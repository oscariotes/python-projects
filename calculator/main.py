from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2


def calucalator():
    print(logo)



    num1 = float(input('What is the first number? '))

    operations = {
    '+': add, 
    '-' : subtract, 
    '*' : multiply, 
    '/': devide,
    }

    for symbols in operations:
        print(symbols)

    continue_calculation = True
    while continue_calculation:
        num2 = float(input('What is the next number? '))
        choose = str(input('Please choose the operation: '))
        answer = operations[choose](num1, num2)
        print(f'{num1} {choose} {num2} = {answer}')

        ask_user = str(input('Do you wannt to continue with another operation? y or n for new calculation ')).lower()
        if ask_user == 'n':
            continue_calculation = False
            calucalator()

        elif ask_user == 'y':
            num1 = answer

calucalator()







