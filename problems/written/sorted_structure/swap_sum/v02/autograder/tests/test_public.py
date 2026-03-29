import swap_sum


DEFAULT_VISIBILITY = 'visible'


def test_on_simple_example():
    """Public test: there is a possible swap."""
    A = [1, 6, 50]
    B = [4, 24, 35]

    your_result = swap_sum.swap_sum(A, B)

    # (1, 0) is a valid swap
    assert your_result is not None

    i, j = your_result
    sum_of_A_after_swapping = sum(A) + B[j] - A[i]
    sum_of_B_after_swapping = sum(B) + A[i] - B[j]

    assert sum_of_A_after_swapping + 10 == sum_of_B_after_swapping


def test_on_simple_negative_example():
    """Public test: there is no possible swap."""

    A = [5]
    B = [3]

    your_result = swap_sum.swap_sum(A, B)

    assert your_result is None


def test_check_that_lists_not_altered():
    """Public test: check that A and B are not changed."""
    # your code should not alter A and B. If it does, there's a good chance you're
    # using an approach with sub-optimal time complexity

    A = [1, 6, 50]
    B = [4, 24, 35]

    A_original = A.copy()
    B_original = B.copy()

    your_result = swap_sum.swap_sum(A, B)

    assert A == A_original
    assert B == B_original
