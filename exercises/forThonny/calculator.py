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
'+': add(n1=num1, n2=num2), 
'-' : subtract(n1=num1, n2=num2), 
'*' : multiply(n1=num1, n2=num2), 
'/': devide(n1=num1, n2=num2),
}

for symbols in operations:
    print(symbols)
    
choose = str(input('Please choose the operation: '))


operation_symbol = ''

for symbols in operations:
    if choose in operations:
        operation_symbol = choose



answer = operations[choose]   
    

 
    


print(f'{num1} {operation_symbol} {num2} = {answer}')
