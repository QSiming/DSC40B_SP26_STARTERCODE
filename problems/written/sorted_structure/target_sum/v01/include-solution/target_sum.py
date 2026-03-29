def target_sum(A,B,t):
    """
        A and B are list of sorted numbers 
        t is the target to be found
    """ 

    # since the two arrays are sorted. we start with 
    # initializing one pointer with the first index of any one array
    # and the other pointer with the last index of the other array
    A_i, B_i = 0, len(B) - 1
    
    while A_i < len(A) and B_i >= 0:
        
        current_sum = A[A_i] + B[B_i]

        # found target then return the values a and b
        if current_sum == t:
            return (A[A_i], B[B_i])


        elif current_sum < t:
            # current_sum was smaller! since we are incrementing the values in A
            # and decrementing the values in B
            # Increasing A_i will mean that the element in A that we get next will
            # increase our current sum, which is what is expected to find the target
            A_i += 1
        else:
            # current sum was larger!
            # Decreasing B_i will mean that the element in B that we get next will
            # decrease our current sum, which is what is expected to find the target
            B_i -= 1
             
    return None