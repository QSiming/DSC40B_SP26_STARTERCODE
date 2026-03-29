def median(numbers):
    """computes the median. `numbers` is an array of n numbers"""
    n = len(numbers)
    for x in numbers:
        less = 0
        more = 0
        for y in numbers:
            if y <= x:
                less += 1
            if y >= x:
                more += 1
        if less >= n/2 and more >= n/2:
            return x
