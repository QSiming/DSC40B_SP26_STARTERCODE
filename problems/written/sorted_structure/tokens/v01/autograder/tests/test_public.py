import allocate_tokens


DEFAULT_VISIBILITY = 'visible'


def test_on_example_from_problem_writeup():
    """Public test: late = [20, 75] and n_tokens = 2."""
    your_result = allocate_tokens.allocate_tokens(late=[20, 75], n_tokens=2)

    # the best strategy is to "flip" the 75 point homework with the first token,
    # and to use the second token for 50 points of extra credit, resulting in 125 points
    assert your_result == 125

def test_when_there_are_no_lates():
    """Public test: there are no lates."""
    your_result = allocate_tokens.allocate_tokens(late=[], n_tokens=2)

    # both tokens should be used for extra credit, for a total of 50 + 30 = 80 points
    assert your_result == 80

def test_when_there_are_no_tokens():
    """Public test: there are no tokens."""
    your_result = allocate_tokens.allocate_tokens(late=[50, 100], n_tokens=0)

    # Professor says: ``sorry, nothing we can do for you : (''
    assert your_result == 0
