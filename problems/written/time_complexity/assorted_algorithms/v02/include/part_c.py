def mode(data):
    """
    computes the mode
    `data` is a list of size n
    """
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
    return mode
