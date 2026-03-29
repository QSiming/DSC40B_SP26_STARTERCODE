def find_mode(arr):
"""Should return the mode of arr, along with its frequency."""
    if len(arr) == 1:
        return arr[0], 1
    middle = math.floor(len(arr) / 2)
    left_mode, left_freq = find_mode(arr[:middle])
    right_mode, right_freq = find_mode(arr[middle:])
    if left_freq > right_freq:
        return left_mode, left_freq
    else:
        return right_mode, right_freq
