import math

def find_first_geq(arr, x, *, start=0, stop=None):
    """Find first index that is >= x in arr[start:stop], where arr is sorted"""
    if stop is None:
        stop = len(arr)

    if stop - start == 1:
        if arr[start] >= x:
            return start
        else:
            return stop

    middle = math.floor((start + stop) / 2)
    if arr[middle] >= x:
        return find_first_geq(arr, x, start=start, stop=middle)
    else:
        return find_first_geq(arr, x, start=middle, stop=stop)

def find_first_gt(arr, x, *, start=0, stop=None):
    """Find first index that is > x in arr[start:stop], where arr is sorted"""
    if stop is None:
        stop = len(arr)

    if stop - start == 1:
        if arr[start] > x:
            return start
        else:
            return stop

    middle = math.floor((start + stop) / 2)
    if arr[middle] > x:
        return find_first_gt(arr, x, start=start, stop=middle)
    else:
        return find_first_gt(arr, x, start=middle, stop=stop)

def logcount(arr, a, b):
    if len(arr) == 0: return 0
    start = find_first_geq(arr, a)
    stop = find_first_gt(arr, b)
    return max(stop - start, 0)
