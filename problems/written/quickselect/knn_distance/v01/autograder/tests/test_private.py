import time
import math

import knn_distance


DEFAULT_VISIBILITY = "after_due_date"


def test_on_large_number_of_points():
    """Large number of points"""
    points = list(range(200))

    your_distance, your_point = knn_distance.knn_distance(points, 52.4, 1)
    assert math.isclose(your_distance, 0.4)
    assert your_point == 52

    points = list(range(200))  # needed to allow modification of input
    your_distance, your_point = knn_distance.knn_distance(points, 52.4, 7)
    assert math.isclose(your_distance, 3.4)
    assert your_point == 49


def test_with_ties_returns_arbitrary_point():
    """With ties."""
    points = [30, 20, 10, 40]
    your_distance, your_point = knn_distance.knn_distance(points, 15, 1)
    assert your_distance == 5
    assert (your_point == 10) or (your_point == 20)


def test_k_equals_len_arr():
    """Asking for the furthest point."""
    points = [30, 20, 10, 40, 50, 60, 999]
    your_distance, your_point = knn_distance.knn_distance(points, 2, len(points))
    assert your_distance == 997
    assert your_point == 999


def test_efficiency():
    """Running your code on a very large input to test efficiency."""
    points = list(range(999_999))

    start = time.time()
    your_distance, your_point = knn_distance.knn_distance(points, 100_000.2, k=10_000)
    stop = time.time()

    elapsed_time = stop - start

    assert math.isclose(your_distance, 4999.8)
    assert your_point == 10_5000

    assert elapsed_time < 10
