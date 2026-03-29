import math
def ternary_search(arr, t, start, stop):
    """
    Return the index of t in arr[start:stop]
    assume arr is sorted
    """
    if stop - start <= 0:
        return None
    n = stop - start
    left_ix = math.floor(start + (stop - start) / 3)
    right_ix = math.floor(start + 2 * (stop - start) / 3)
    if arr[left_ix] == t:
        return left_ix
    if arr[right_ix] == t:
        return right_ix
    if t < arr[left_ix]:
        return ternary_search(arr, t, start, left_ix)
    elif t > arr[right_ix]:
        return ternary_search(arr, t, right_ix + 1, stop)
    else:
        return ternary_search(arr, t, left_ix, right_ix)
