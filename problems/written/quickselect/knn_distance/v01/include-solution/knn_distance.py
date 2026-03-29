import random


def knn_distance(arr, q, k):
    """Compute the kth nearest point and the distance to it."""

    # compute the distance between x and q
    def dist(x):
        return abs(x - q)

    # there's a small trick here that allows us to use `quickselect` from
    # lecture unmodified; instead of passing in a list of numbers, we pass in a
    # list of (distance, point) tuples. when Python compares two tuples, it
    # compares their first elements; if there is a tie, it then compares their
    # second elements, and so on. here, quickselect will find the pair with the
    # kth smallest first element, which is exactly what we need to return.
    distance_point_pairs = [(dist(x), x) for x in arr]
    return quickselect(distance_point_pairs, k, 0, len(arr))


# everything below is code for quickselect that comes unmodified from lecture

def in_place_partition(arr, start, stop, pivot_ix):
    def swap(ix_1, ix_2):
        arr[ix_1], arr[ix_2] = arr[ix_2], arr[ix_1]

    pivot = arr[pivot_ix]
    swap(pivot_ix, stop-1)
    middle_barrier = start
    for end_barrier in range(start, stop - 1):
        if arr[end_barrier] < pivot:
            swap(middle_barrier, end_barrier)
            middle_barrier += 1
        # else: do nothing
    swap(middle_barrier, stop-1)
    return middle_barrier


def quickselect(arr, k, start, stop):
    """Find kth order statistics in arr[start, stop]"""
    pivot_ix = random.randrange(start, stop)
    pivot_ix = in_place_partition(arr, start, stop, pivot_ix)
    pivot_order = pivot_ix + 1
    if pivot_order == k:
        return arr[pivot_ix]
    elif pivot_order < k:
        return quickselect(arr, k, pivot_ix+1, stop)
    else:
        return quickselect(arr, k, start, pivot_ix)
