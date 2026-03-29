def product(numbers):
    """Returns the product of all elements in numbers."""
    if len(numbers) == 0:
        return 1
    return numbers[0] * product(numbers[1:])
