def also_the_variance(data):
    """
    computes the variance of `data`
    `data` is a list of size n
    """
    mu = sum(data) / len(data)
    total = 0
    for x in data:
        total += (x - mu)**2
    return total / len(data)
