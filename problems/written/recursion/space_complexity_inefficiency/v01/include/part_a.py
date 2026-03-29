def summation(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + summation(numbers[1:])
