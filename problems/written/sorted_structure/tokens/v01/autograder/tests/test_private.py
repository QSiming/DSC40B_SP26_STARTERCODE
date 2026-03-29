import time

from autogradescope.decorators import weight

import allocate_tokens



DEFAULT_VISIBILITY = 'after_due_date'



def test_with_only_one_token():
    """Test with one token."""
    late = [40, 10, 20, 100]
    n_tokens = 1

    your_answer = allocate_tokens.allocate_tokens(late, n_tokens)

    assert your_answer == 100


def test_with_extra_tokens():
    """Test with extra tokens."""
    late = [40, 10, 20, 100]
    n_tokens = 9

    your_answer = allocate_tokens.allocate_tokens(late, n_tokens)

    assert your_answer == (100 + 40 + 20 + 10) + (50 + 30 + 20 + 10 + 10)

def test_with_very_valuable_lates():
    """Test with extra tokens."""
    late = [100, 100, 100, 100]
    n_tokens = 4

    your_answer = allocate_tokens.allocate_tokens(late, n_tokens)

    assert your_answer == 400

def test_with_not_very_valuable_lates():
    """Test with extra tokens."""
    late = [1, 1, 1, 1]
    n_tokens = 4

    your_answer = allocate_tokens.allocate_tokens(late, n_tokens)

    assert your_answer == 50 + 30 + 20 + 10

@weight(4)
def test_efficiency():
    """Test empirically that the code is efficient (i.e., not quadratic)."""
    # to test the efficiency of your code, we'll create a very large amount of late
    # assignments, each with a very high point value, and n_tokens = len(late).
    # This forces your code to use all of the tokens on flipping the assignments.
    # Your code can be correct but inefficient if it doesn't sort the lates. For instance,
    # it could find the max late at each iteration, which would take quadratic time
    # instead of Theta(n log n).
    late = [100] * 100_000

    start = time.time()
    your_answer = allocate_tokens.allocate_tokens(late, n_tokens=len(late))
    stop = time.time()

    # if your code takes more than, say, half a second, it probably isn't linear time
    elapsed_time = stop - start
    assert elapsed_time < .5
