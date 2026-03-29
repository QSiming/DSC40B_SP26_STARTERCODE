def foo(numbers):
    """Assume `numbers` is a Python `set` containing n numbers."""
    count = 0
    for x in numbers:
        if -x in numbers:
            count += 1

    return count / len(numbers)


print(foo({1, 2, 3, -2, -1}))
