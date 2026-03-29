import knn_distance


DEFAULT_VISIBILITY = 'visible'


def test_on_simple_example_1():
    """Public test 1."""
    assert knn_distance.knn_distance([3, 10, 52, 15], 19, 1) == (4, 15)


def test_on_simple_example_2():
    """Public test 2."""
    assert knn_distance.knn_distance([3, 10, 52, 15], 19, 2) == (9, 10)


def test_on_simple_example_3():
    """Public test 3."""
    assert knn_distance.knn_distance([3, 10, 52, 15], 19, 3) == (16, 3)
