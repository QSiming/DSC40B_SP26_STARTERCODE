import math

def mediansort(arr, start, stop):
    """Claims to sort the array, in-place."""
    if stop - start <= 1:
        return

    # finds the index of the median of arr[start:stop]
    median_ix = find_median(arr, start, stop)

    middle_ix = math.floor((start + stop) / 2)

    # move the median to the middle by swapping
    arr[median_ix], arr[middle_ix] = arr[middle_ix], arr[median_ix]

    # recurse on the left and right halves
    mediansort(arr, start, middle_ix)
    mediansort(arr, middle_ix + 1, stop)


def find_median(arr, start, stop):
    """Finds the index of a median of the elements in arr[start:stop]."""
    numbers = arr[start:stop]
    median = sorted(numbers)[len(numbers) // 2]
    for i in range(start, stop):
        if arr[i] == median:
            return i


import random
s = random.randint(10, 100)
arr = [random.randint(0, 1000) for _ in range(s)]
mediansort(arr, 0, len(arr))
print(arr)
