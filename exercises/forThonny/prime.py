n = int(input('What is the number? '))

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