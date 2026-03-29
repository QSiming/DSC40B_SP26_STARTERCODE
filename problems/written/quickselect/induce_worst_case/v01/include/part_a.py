def in_place_partition(arr, start, stop, pivot_ix):
    def swap(ix_1, ix_2):
        arr[ix_1], arr[ix_2]=arr[ix_2], arr[ix_1]
    pivot = arr[pivot_ix]
    swap(pivot_ix, stop-1)
    middle_barrier=0
    for end_barrier in range(stop-1):
        if arr[end_barrier]<pivot:
            swap(middle_barrier, end_barrier)
            middle_barrier+=1
        # else:
            # do nothing
    swap(middle_barrier, stop-1)
    return middle_barrier

def quickselect(arr, k, start, stop):
    pivot_ix=random.randrange(start, stop)
    pivot_ix=in_place_partition(arr, start, stop, pivot_ix)
    pivot_order=pivot_ix+1
    if pivot_order==k:
        return arr[pivot_ix]
    elif pivot_order<k:
        return quickselect(arr, k, pivot_ix+1, stop)
    else:
        return quickselect(arr, k, start, pivot_ix)
