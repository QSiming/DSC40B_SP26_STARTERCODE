def mode(data):
    """computes the mode. `data` is an array of n numbers."""
    mode = None
    largest_frequency = 0
    for x in data:
        count = 0
        for y in data:
            if x == y:
                count += 1
        if count > largest_frequency:
            largest_frequency = count
            mode = x
        if count > n/2:
            return mode
    return mode
