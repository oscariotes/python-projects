x = [1, 2, 3, 4]

def grow(arr):
    num = 1
    for i in arr:
        num *= i
    return num

grow(x)