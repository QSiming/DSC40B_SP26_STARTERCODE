def partition(arr, start, stop):
    left=[]
    right=[]
    pivot=arr[stop-1]
    for ix in range(start,stop):
        if arr[ix]>pivot:
            left.append(arr[ix])
        else if arr[ix]<pivot:
            right.append(arr[ix])
    ix=start
    for x in left:
        arr[ix]=x
        ix+=1
    pivot_ix=ix
    arr[ix]=pivot
    ix+=1.
    for x in right:
        arr[ix]=x
        ix+=1
    return pivot_ix
