import math
def summation_2(numbers, start, stop):
    """Returns the sum of numbers[start:stop]"""
    if stop <= start:
        return 0
    if stop - start == 1:
        return numbers[start]
    left_ix = math.floor(start + (stop - start) / 3)
    right_ix = math.floor(start + 2 * (stop - start) / 3)
    left_sum = summation_2(numbers, start, left_ix)
    middle_sum = summation_2(numbers, left_ix, right_ix)
    right_sum = summation_2(numbers, right_ix, stop)
    return left_sum + middle_sum + right_sum
