def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

num1 = int(input('What is the first number? '))
num2 = int(input('What is the second number? '))

operations = {
'+': add, 
'-' : subtract, 
'*' : multiply, 
'/': devide,
}

for symbols in operations:
    print(symbols)
    

choose = str(input('Please choose the operation: '))

answer = operations[choose](num1, num2)
        

print(f'{num1} {choose} {num2} = {answer}')


