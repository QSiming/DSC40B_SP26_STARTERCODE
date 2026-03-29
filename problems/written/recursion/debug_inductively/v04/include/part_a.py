def max_arr(arr):
    max1 = arr[0]
    max2 = max_arr(arr[1:])
    if(max1 > max2):
        return max1
    else:
        return max2
