def swap_sum(A,B):
    
    target = (sum(A) - sum(B))/2
    i = 0
    j = 0
    while(True):
        if A[i]-B[j] == target:
            return (A[i],B[j])
        elif A[i]-B[j] < target:
            i += 1
        else:
            j += 1
