import balance

from autogradescope.decorators import weight

import numpy as np


DEFAULT_VISIBILITY = 'visible'


@weight(1)
def test_returns_pair_of_ints():
    """Tests that your code returns a pair of integers."""
    # given
    left = [1, 2, 3]
    right = [4, 5, 6]

    # when
    left_ix, right_ix = balance.balance(left, right)

    # then 
    assert isinstance(left_ix, int)
    assert isinstance(right_ix, int)

def new_total_weights(left, right, left_ix, right_ix):
    left_weight = sum(left) - left[left_ix] + right[right_ix]
    right_weight = sum(right) - right[right_ix] + left[left_ix]
    return left_weight, right_weight

@weight(1)
def test_on_example_given_in_homework():
    left = [4, 8, 12]
    right = [6, 15]

    left_ix, right_ix = balance.balance(left, right)

    assert left_ix == 1
    assert right_ix == 0
