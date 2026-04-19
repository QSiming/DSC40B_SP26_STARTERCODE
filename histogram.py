def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    
    # points = [1,2,3, 6,7, 9,10,11]
    # bins = [(0,4), (4,8), (8,12)]
    out = []
    total_num = len(points)     # how many numbers total
    i = 0   # for go over the list

    for a, b in bins:
        count = 0

        while i < total_num and points[i] < b:  
            count += 1       # use count find length for bin 
            i += 1

        bin_width = (b-a)
        density = count / (total_num * bin_width)   
        out.append(density)
    
    return out
