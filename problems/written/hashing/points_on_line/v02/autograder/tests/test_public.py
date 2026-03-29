import max_points_on_line

DEFAULT_VISIBILITY = 'visible'


def test_1():
    """Public test: test case from the homework PDF"""
    X = [
        (1, 1),
        (3, 1),
        (5, 2),
        (3, 6),
        (1, 7),
        (7, 4),
        (9, 3),
        (9, 9)
    ]

    p = (5, 5)

    your_result = max_points_on_line.max_points_on_line(X, p)

    # the answer is 4
    assert isinstance(your_result, int)
    assert your_result == 4


def test_2():
    """Public test: return 0 when X is empty"""
    X = []

    p = (1, 1)

    your_result = max_points_on_line.max_points_on_line(X, p)

    # the answer is 0
    assert isinstance(your_result, int)
    assert your_result == 0
