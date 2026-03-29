from autogradescope.decorators import weight, timeout
import numpy as np
import time

import histogram


DEFAULT_VISIBILITY = "after_published"


def slow_solution(points, bins):
    """This is a solution that has the incorrect time complexity.

    We use this to determine the time cutoff for the efficiency test.

    """
    result = []
    n = len(points)

    for bin_start, bin_end in bins:
        bin_count = 0
        for point in points:
            if bin_start <= point < bin_end:
                bin_count += 1
        result.append(bin_count / (n * (bin_end - bin_start)))

    return result


def solution(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    result = []
    n = len(points)

    point_ix = 0

    for bin_start, bin_end in bins:
        bin_count = 0
        while point_ix < len(points) and points[point_ix] < bin_end:
            point_ix += 1
            bin_count += 1
        result.append(bin_count / (n * (bin_end - bin_start)))

    return result


def test_works_with_larger_inputs():
    """Works on 100 points."""
    np.random.seed(42)
    points = np.random.uniform(0, 10, size=100)
    points = np.sort(points)
    bins = [(0, 3), (3, 8), (8, 10)]
    your_answer = histogram.histogram(points, bins)
    correct_answer = solution(points, bins)
    assert np.allclose(your_answer, correct_answer)


def test_works_with_much_larger_inputs():
    """Works on 1000 points."""
    np.random.seed(42)
    points = np.random.uniform(0, 10, size=1000)
    points = np.sort(points)
    bins = [(0, 3), (3, 8), (8, 10)]
    your_answer = histogram.histogram(points, bins)
    correct_answer = solution(points, bins)
    assert np.allclose(your_answer, correct_answer)


def make_a_lot_of_bins(start, stop, n_bins):
    """This makes n_bins ranging from start to stop."""
    bins = []
    for i in range(n_bins):
        bin_start = start + i * (stop - start) / n_bins
        bin_end = start + (i + 1) * (stop - start) / n_bins
        bins.append((bin_start, bin_end))
    return bins


@weight(2)
@timeout(200)
def test_efficiency():
    """Tests that your code has the expected time complexity."""
    # There's no easy way to check that your code has exactly the right time complexity
    # with an autograder, but we can time it on a large input. Code has takes the correct
    # time complexity of Theta(n) should take much less time than code that has a
    # time complexity of Theta(n^2), so we just check that it's not too slow.
    np.random.seed(42)
    n_points = 50_000
    points = np.random.uniform(0, 10, size=n_points)
    points = np.sort(points)
    bins = make_a_lot_of_bins(start=0, stop=11, n_bins=n_points // 10)

    start = time.time()
    your_answer = histogram.histogram(points, bins)
    finish = time.time()

    time_taken = finish - start
    assert time_taken < 1, "Your code took too long, and likely has the wrong time complexity."
