#  ([9]), 9

x = [9, 9]

def max(arr):
    if not arr:  # Check if the array is empty
        return None  # Return None if the array is empty
    
    num = arr[0]  # Initialize num with the first element of the array
    for i in arr:
        if i > num:
            num = i
    return num
print(max(x)

def min(arr):
    if not arr:  # Check if the array is empty
        return None  # Return None if the array is empty
    
    num = arr[0]  # Initialize num with the first element of the array
    for i in arr:
        if i < num:
            num = i
    return num

print(min(x))

