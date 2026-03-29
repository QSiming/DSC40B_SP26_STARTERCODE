import histogram
import numpy as np

DEFAULT_VISIBILITY = "visible"


def test_simple_example():
    """Works on simple example."""
    points = [1, 2, 3, 6, 7, 9, 10, 11]
    bins = [(0, 4), (4, 8), (8, 12)]
    your_answer = histogram.histogram(points, bins)
    correct_answer = [3/32, 1/16, 3/32]
    assert np.allclose(your_answer, correct_answer)


def test_unequal_bin_sizes():
    """Test when bins are not all the same size."""
    points = [1, 2, 3, 6, 7, 8]
    bins = [(0, 4), (4, 9)]
    your_answer = histogram.histogram(points, bins)
    correct_answer = [0.125, 0.1]
    assert np.allclose(your_answer, correct_answer)


def test_bins_are_closed_on_left_open_on_right():
    """Bins are closed on the left and open on the right, like [5, 10)."""
    # 3 is right on the boundary of the bins; it should be included in the second
    # bin since the bins are closed on the left and open on the right.
    points = [1, 2, 3, 4, 5, 6]
    bins = [(0, 3), (3, 8)]
    your_answer = histogram.histogram(points, bins)
    correct_answer = [1 / 9, 2 / 15]
    assert np.allclose(your_answer, correct_answer)
