import time

from autogradescope.decorators import weight

import swap_sum



DEFAULT_VISIBILITY = 'after_due_date'


def test_positive_example_1():
    """There's a valid swap, A and B are same length."""

    A = [-30, -20, 10, 60]
    B = [-10, 5, 15, 60]

    sum_A = sum(A)
    sum_B = sum(B)

    your_result = swap_sum.swap_sum(A, B)

    # (0, 0) is a valid swap
    assert your_result is not None

    i, j = your_result
    sum_of_A_after_swapping = sum_A + B[j] - A[i]
    sum_of_B_after_swapping = sum_B + A[i] - B[j]

    assert sum_of_A_after_swapping + 10 == sum_of_B_after_swapping


def test_positive_example_2():
    """There's a valid swap, A and B different length."""

    A = [10, 20, 30, 100, 150, 470]
    B = [-50, 100, 200]

    sum_A = sum(A)
    sum_B = sum(B)

    your_result = swap_sum.swap_sum(A, B)

    # (5, 2) is a valid swap
    assert your_result is not None

    i, j = your_result
    sum_of_A_after_swapping = sum_A + B[j] - A[i]
    sum_of_B_after_swapping = sum_B + A[i] - B[j]

    assert sum_of_A_after_swapping + 10 == sum_of_B_after_swapping


def test_positive_example_3():
    """There's a valid swap, A and B are longer."""

    A = [0, 15, 18, 21, 23, 24, 35]
    B = [9, 10, 21, 22, 27, 29]

    sum_A = sum(A)
    sum_B = sum(B)

    your_result = swap_sum.swap_sum(A, B)

    # (4, 0) is a valid swap
    assert your_result is not None

    i, j = your_result
    sum_of_A_after_swapping = sum_A + B[j] - A[i]
    sum_of_B_after_swapping = sum_B + A[i] - B[j]

    assert sum_of_A_after_swapping + 10 == sum_of_B_after_swapping


def test_negative_example_1():
    """There's no valid swap, A and B are same length."""

    A = [0, 15, 18, 21, 23, 24, 35]
    B = [9, 10, 21, 22, 27, 29, 100]

    your_answer = swap_sum.swap_sum(A, B)
    assert your_answer is None


def test_negative_example_2():
    """There's no valid swap, A and B are both singletons."""
    A = [5]
    B = [3]

    your_answer = swap_sum.swap_sum(A, B)
    assert your_answer is None


@weight(4)
def test_efficiency():
    """Test empirically that the code is efficient (i.e., not quadratic)."""
    A = list(range(100_000))
    B = list(range(100_000))

    # this makes sure that there is no possible swap, which is the worst case
    A.append(.5)

    start = time.time()
    your_answer = swap_sum.swap_sum(A, B)
    stop = time.time()

    # if your code takes more than, say, a second, it probably isn't linear time
    # check to see if you're calling sum() in your while-loop; if you are, your
    # coide probably takes quadratic time!
    elapsed_time = stop - start
    assert elapsed_time < 5
