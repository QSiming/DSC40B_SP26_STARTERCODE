def swap_sum(A, B):
    """Swaps two elements in two sorted arrays to obtain a target sum 
    difference of 10.

    Assumes that both arrays are sorted in ascending order and only 
    contain integers.

    """
    # A = [1, 6, 50]     B = [4, 24, 35]
    # sum A - sum B = -10 (after swap)   or     sum B - sum A = 10 (after swap)
    # (sum B - sum A - 10) / 2  = B[j] - A[i]
    sumA = sum(A)
    sumB = sum(B)

    diff = sumB - sumA - 10

    
    if diff % 2 != 0:    # check for eligiablity 
        return None

    target = diff // 2

    i = 0
    j = 0

    while i < len(A) and j < len(B):     
        current = B[j] - A[i]

        if current == target:
            return (i, j)
        elif current < target:
            j += 1
        else:
            i += 1

    return None
