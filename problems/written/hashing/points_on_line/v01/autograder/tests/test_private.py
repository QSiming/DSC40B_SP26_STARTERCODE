from autogradescope.decorators import weight
import time

import max_points_on_line

DEFAULT_VISIBILITY = 'after_due_date'


@weight(1)
def test_1():
    """large number of points"""
    X = [
        (-2, 1),
        (4, 1),
        (3, -1),
        (-3, 3),
        (-2, 1),
        (5, -2),
        (-2, -3),
        (-4, -5),
        (0, 3),
        (-3, 4),
        (-4, -3),
        (4, -1),
        (-4, -3),
        (4, -4),
        (-5, 5)
    ]

    p = (4, 5)

    your_result = max_points_on_line.max_points_on_line(X, p)

    correct_answer = 3

    # the answer is 3
    assert your_result == correct_answer


@weight(1)
def test_2():
    """negative points with negative coordinates"""
    X = [
        (5, 2),
        (-1, 4),
        (5, -4)
    ]

    p = (1, -6)

    your_result = max_points_on_line.max_points_on_line(X, p)

    correct_answer = 1

    # the answer is 1
    assert your_result == correct_answer


@weight(1)
def test_3():
    """all points on same lines"""
    X = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]

    p = (0, 0)

    your_result = max_points_on_line.max_points_on_line(X, p)

    correct_answer = 4

    # the answer is 4
    assert your_result == correct_answer


@weight(1)
def test_4():
    """all points on same line, p is on different line"""
    X = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]

    p = (1, 2)

    your_result = max_points_on_line.max_points_on_line(X, p)

    correct_answer = 1

    # the answer is 1
    assert your_result == correct_answer



@weight(1)
def test_5():
    """a line with points to the left of p and points to the right"""

    # 3 points on same line vs. 4 points on the same line
    X = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (-1, -1),
        (-2, -2),
        (-3, -3)
    ]

    p = (0, 0)

    your_result = max_points_on_line.max_points_on_line(X, p)

    correct_answer = 7

    # the answer is 7
    assert your_result == correct_answer


@weight(1)
def test_6():
    """a corner case: the query point equals a point in X"""
    X = [
        (1, 1),
        (2, 2),
    ]

    p = (1, 1)

    your_result = max_points_on_line.max_points_on_line(X, p)

    correct_answer = 2

    # the answer is 7
    assert your_result == correct_answer


@weight(4)
def test_efficiency():
    """Test empirically that the code is efficient (i.e., linear time)."""
    X = list(zip(range(100_000), range(100_000)))
    p = (0, 0)
    # this makes sure that there is no possible swap, which is the worst case

    start = time.time()
    max_points_on_line.max_points_on_line(X, p)
    stop = time.time()

    # if your code takes more than, say, a second, it probably isn't linear time
    elapsed_time = stop - start
    assert elapsed_time < 1
