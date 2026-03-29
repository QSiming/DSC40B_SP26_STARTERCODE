def product(numbers):
    """Should return the product of all elements in numbers."""
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] * product(numbers[1:])
