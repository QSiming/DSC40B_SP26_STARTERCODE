import random

def knn_distance(arr, q, k):
    """Compute the kth nearest point and the distance to it."""
    # TODO: Implement the knn_distance function
    def quickselect(pairs, k):
        if len(pairs) == 1:
            return pairs[0]
            
        pivot = random.choice(pairs)
        
        left = [x for x in pairs if x[0] < pivot[0]]
        middle = [x for x in pairs if x[0] == pivot[0]]
        right = [x for x in pairs if x[0] > pivot[0]]
        
        if k < len(left):
            return quickselect(left, k) # left
            
        elif k < len(left) + len(middle):   # middle
            return middle[0]
 
        else:     # right
            return quickselect(right, k - len(left) - len(middle))

    pairs = []
    
    for x in arr:
        pairs.append((abs(q - x),x))

    
    return quickselect(pairs, k - 1)