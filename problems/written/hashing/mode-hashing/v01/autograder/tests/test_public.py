import mode

DEFAULT_VISIBILITY = 'visible'


def test_on_example_from_problem():
    numbers = [4, 5, 8, 3, 4, 2, 4, 5, 5, -2]
    result = mode.mode(numbers)
    assert result in {4, 5}
