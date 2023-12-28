x = [1, 2, 2]

def square_sum(numbers):
    num = []
    for i in numbers:
        num.append(i**2)
    return sum(num)

print(square_sum(x))
        
        