def find_minimum(arr, start_ix):
    """
    Find the value and index of the minimum element 
    in arr[start_ix:].
    
    Assumes that len(arr) > 0.
    """
    start_value = arr[start_ix]
    if start_ix == len(arr) - 1:
        return start_value, start_ix

    tail_min_value, tail_min_ix = find_minimum(arr, start_ix+1)
    if tail_min_value < start_value:
        return tail_min_value, tail_min_ix
    else:
        return start_value, start_ix


def selection_sort(arr, start_ix):
    """Sort arr[start_ix:]."""
    if start_ix >= len(arr) - 1:
        return
    min_value, min_ix = find_minimum(arr, start_ix)
    arr[start_ix], arr[min_ix] = arr[min_ix], arr[start_ix] # swap
    selection_sort(arr, start_ix+1)
