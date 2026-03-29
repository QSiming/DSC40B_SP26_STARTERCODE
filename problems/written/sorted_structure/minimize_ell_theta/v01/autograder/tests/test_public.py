from autogradescope.decorators import weight, visibility

# import student's code
import min_ell_theta


DEFAULT_VISIBILITY = 'visible'


def test_part_a_on_simple_example():
    """Part a) Works on a simple example."""

    data = [5, 3, 6, 7, 1]
    colors = ['red', 'blue', 'red', 'red', 'blue']

    actual = min_ell_theta.learn_theta(data, colors)
    assert actual < 5
    assert actual >= 3


def test_part_b_on_simple_example():
    """Part b) Works on a simple example."""
    
    data = [5, 3, 6, 7, 1, 0]
    colors = ['red', 'blue', 'red', 'red', 'blue', 'red']
    actual = min_ell_theta.compute_ell(data, colors, 3.5)
    assert actual == 1


def test_part_c_on_simple_example():
    """Part c) Works on a simple example."""

    data = [5, 3, 6, 7, 1]
    colors = ['red', 'blue', 'red', 'red', 'blue']

    actual = min_ell_theta.minimize_ell(data, colors)
    assert actual < 5
    assert actual >= 3


def test_minimize_ell_sorted_on_simple_example():
    """Works on a simple example."""

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    colors = ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'blue', 'red', 'red']

    result = min_ell_theta.minimize_ell_sorted(data, colors)
    assert result >= 4
    assert result < 5
