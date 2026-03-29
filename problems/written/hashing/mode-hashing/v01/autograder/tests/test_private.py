import mode

DEFAULT_VISIBILITY = 'after_due_date'

def test_on_a_large_list():
    # this list contains [-1, -2, -2, -3, -3, -3, ..., -9999]
    numbers = [-i for i in range(1, 10000) for _ in range(i)]

    result = mode.mode(numbers)

    assert result == -9999


def test_on_a_list_with_one_item():
    result = mode.mode([42])
    assert result == 42


def test_on_a_list_with_two_items_that_are_the_same():
    result = mode.mode([13, 13])
    assert result == 13

def test_on_another_non_trivial_example():
    result = mode.mode([1, 2, 3, 1, 5, 5, 2, 3, 1, 2, 5, 5, 3])
    assert result == 5
