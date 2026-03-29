import math

def new_binary_search(arr, start, stop, target):
    if stop <= start:
        return None

    middle = math.ceil((start + stop) / 2)

    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return new_binary_search(arr, middle + 1, stop, target)
    else:
        return new_binary_search(arr, start, middle, target)

arr = [1]
new_binary_search(arr, 0, len(arr)-1, 5)
print(arr)
