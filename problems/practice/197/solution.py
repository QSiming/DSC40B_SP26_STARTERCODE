import math


def find_minimum_in_rotated_sorted(arr, start=None, end=None):
    # Base case: If the array is not rotated
    if start is None:
        start = 0

    if end is None:
        end = len(arr) - 1

    if end < start:
        return arr[0]

    # If there is only one element left
    if end == start:
        return arr[start]

    # Find the middle index
    mid = (start + end) // 2

    # Check if the middle element is the minimum
    if arr[mid + 1] < arr[mid]:
        return arr[mid + 1]

    # Check if the mid element is greater than the start element
    if arr[start] < arr[mid]:
        # The minimum is in the right half
        return find_minimum_in_rotated_sorted(arr, mid, end)
    else:
        # The minimum is in the left half
        return find_minimum_in_rotated_sorted(arr, start, mid - 1)


# make a random sorted array
import random

arr = sorted([random.randrange(100) for _ in range(6)])
# rotate it
# arr = arr[20:] + arr[:20]

print(arr)
print(min(arr))

print(find_minimum_in_rotated_sorted(arr))
