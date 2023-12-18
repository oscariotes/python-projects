import math

n = int(input('What is the number? '))

def is_prime(n):   
    if n < 2:
        return False 
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False         
    return True

if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")         
     
is_prime(n)


def prime(n):
    prime = True
    if n < 2:
        prime = False

    for i in range(2, n):
        if n % 2 == 0:
            prime = False
    if prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")  

prime(n)