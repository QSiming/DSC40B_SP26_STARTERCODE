def is_even(i):
    """Returns True if i is even, False otherwise."""
    return i % 2 == 0

def mystery_partition(numbers):
    def swap(i, j):
        numbers[i], numbers[j] = numbers[j], numbers[i]

    barrier_ix = 0
    for i in range(len(numbers)):
        if is_even(numbers[i]):
            swap(i, barrier_ix)
            if numbers[barrier_ix] > numbers[0]:
                swap(0, barrier_ix)
            barrier_ix += 1


lst = [1, 5, 3, 7, 2, 4, 8, 5, 9, 6, 100]
mystery_partition(lst)
print(lst)
