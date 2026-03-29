import balance
import random
import time

from autogradescope.decorators import weight


DEFAULT_VISIBILITY = "after_published"
DEFAULT_TIMEOUT = 60


def new_total_weights(left, right, left_ix, right_ix):
    left_weight = sum(left) - left[left_ix] + right[right_ix]
    right_weight = sum(right) - right[right_ix] + left[left_ix]
    return left_weight, right_weight


@weight(2)
def test_on_larger_input():
    """Works on a larger input."""
    # given
    left = [18, 21, 331, 454, 502, 554, 624, 759, 855, 974]
    right = [19, 149, 219, 294, 355, 451, 562, 960, 962, 995]

    # when
    left_ix, right_ix = balance.balance(left, right)

    # compute the new total weights by swapping the two values
    left_weight, right_weight = new_total_weights(left, right, left_ix, right_ix)
    difference = abs(left_weight - right_weight)

    # a difference of two can be attained by swapping 624 and 562
    assert difference == 2, f"Your solution had a difference of {difference}."


@weight(2)
def test_with_duplicates():
    """Works when there are duplicate weights."""

    left = [2, 5, 5, 8, 8, 9, 9, 10]
    right = [1, 1, 3, 3, 4, 4, 6, 7]

    left_ix, right_ix = balance.balance(left, right)

    # compute the new total weights by swapping the two values
    left_weight, right_weight = new_total_weights(left, right, left_ix, right_ix)
    difference = abs(left_weight - right_weight)

    # a difference of 9 is possible
    msg = f"A difference of 9 is possible by swapping 7 and 0.\n"
    assert difference == 9, msg


@weight(2)
def test_time_complexity():
    """Check that code takes Theta(n) time."""
    # this test works by giving your code a large input and timing it
    # if your code takes too long, it probably doesn't take linear time.
    # that said, this test is not perfect and could say your code takes
    # more than linear time when it actually doesn't. We try to check
    # for these errors, but please let us know on Campuswire if you're
    # pretty sure that your code takes linear time but this test says
    # otherwise.

    # set the random seed so everyone gets the same inputs
    random.seed(42)
    left = sorted([random.randint(0, 1_000_000_000) for _ in range(1_000_000)])
    right = sorted([random.randint(0, 1_000_000_000) for _ in range(1_000_000)])

    # time your code
    start = time.time()
    balance.balance(left, right)
    end = time.time()

    # check that it took less than 2 seconds
    duration = end - start
    assert duration < 2, "Your code took too long to run."
