def fixedPoint(arr, start, stop):
    if (start >= stop):
        return False
    mid = int((start + stop)/2)
    if(arr[mid] == mid):
        return True
    if(arr[mid] > mid):
        return fixedPoint(arr, start, mid)
    else:
        return fixedPoint(arr, mid+1, stop)
