import math

def iterative_binary_search(arr, target):

    start = 0
    stop = len(arr)

    while (stop - start) > 0:
        print(arr[start])
        middle = math.floor((start + stop) / 2)
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            stop = middle
        else:
            start = middle + 1

    return None

# arr = [-202, -201, -200, -50, -20, -10, -4, -3, 0, 1, 3, 5, 6, 7, 9, 10, 12, 15, 22]
# print(iterative_binary_search(arr, 11))

arr = [3, 4, 7]
print(iterative_binary_search(arr, 5))
