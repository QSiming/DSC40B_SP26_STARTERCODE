def separate_odd_from_even(numbers):
    """Moves the odd numbers to the front, in-place."""
    n = len(numbers)

    def swap(i, j):
        numbers[i], numbers[j] = numbers[j], numbers[i]

    odd_barrier = 0
    even_barrier = n - 1

    while odd_barrier < even_barrier:
        if numbers[odd_barrier] % 2 == 0:
            # the number is even
            swap(odd_barrier, even_barrier)
            even_barrier -= 1
        else:
            # the number is odd
            odd_barrier += 1

# test
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
separate_odd_from_even(numbers)
print(numbers)
