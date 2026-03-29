def index_of_median(numbers):
    """`numbers` is an array of size n"""
    # the median() from part c
    m = median(numbers)
    # the linear_search() from lecture
    return linear_search(numbers, m)
