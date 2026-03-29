from autogradescope.decorators import weight, visibility

# import student's code
import min_ell_theta


DEFAULT_VISIBILITY = 'after_published'


@weight(2)
def test_part_a():
    """Part a test"""

    data_a1 = [3.14, 99, -20, 0, 77.7, 2.718]
    color_a1 = ['red', 'red', 'blue', 'blue', 'red', 'blue']
    actual = min_ell_theta.learn_theta(data_a1, color_a1)
    assert actual < 3.14
    assert actual >= 2.718

    data_a2 = [-3.2, -1000, 60, -6.1, 6.1]
    color_a2 = ['red', 'blue', 'red', 'blue', 'red']
    actual = min_ell_theta.learn_theta(data_a2, color_a2)
    assert actual < -3.2
    assert actual >= -6.1


@weight(2)
def test_part_b():
    """Part b test"""

    data_b1 = [0, -16, 3.2, -6.5, 92, 34]
    color_b1 = ['blue', 'red', 'red', 'blue', 'red', 'blue']
    theta_b1 = 3.2
    actual = min_ell_theta.compute_ell(data_b1, color_b1, theta_b1)
    assert actual == 3

    data_b2 = [0, -16, 3.2, -6.5, 92, 34]
    color_b2 = ['blue', 'red', 'red', 'blue', 'red', 'blue']
    theta_b2 = 0
    actual = min_ell_theta.compute_ell(data_b2, color_b2, theta_b2)
    assert actual == 2


@weight(2)
def test_part_c():
    """Part c test"""

    data_c1 = [-1, 3.5, 10, 7.6, -6, 4.3, -3]
    color_c1 = ['red', 'blue', 'red', 'red', 'blue', 'blue', 'blue']
    actual = min_ell_theta.minimize_ell(data_c1, color_c1)
    assert actual < 7.6
    assert actual >= 4.3

    data_c2 = [0.04, 0.05, 0.01, 0.06, 0.03, 0.02]
    color_c2 = ['blue', 'red', 'blue', 'red', 'blue', 'red']
    actual = min_ell_theta.minimize_ell(data_c2, color_c2)
    assert actual < 0.05
    assert actual >= 0.04



@weight(2)
def test_minimize_ell_sorted_on_simple_example_1():
    """Works on a simple example."""

    data = [1, 2, 3, 4, 5]
    colors = ['blue', 'blue', 'blue', 'red', 'red']

    result = min_ell_theta.minimize_ell_sorted(data, colors)
    assert result >= 3
    assert result < 4

@weight(2)
def test_minimize_ell_sorted_on_simple_example_2():
    """Works on a simple example."""

    data = [2,4,6,8,10,24,48,96,100]
    colors = ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'blue', 'red']

    result = min_ell_theta.minimize_ell_sorted(data, colors)
    assert result >= 8
    assert result < 10

@weight(2)
def test_minimize_ell_sorted_on_simple_example_3():
    """Works on a simple example."""

    data = [1, 2, 3, 4, 5, 6]
    colors = ['blue', 'blue', 'blue', 'red', 'red', 'blue']

    result = min_ell_theta.minimize_ell_sorted(data, colors)
    assert result >= 3
    assert result < 4
