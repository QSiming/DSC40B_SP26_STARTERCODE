
def compute_y_intercept(point, vector):
    """Compute the y-intercept of the line that passes through the given point and has the given vector as its slope.

    Parameters
    ----------
    point
        A 2-tuple of integers representing a point.
    vector
        A 2-tuple of integers representing a vector.

    Returns
    -------
    float

    Example
    -------

    >>> point = (1, 1)
    >>> vector = (2, 3)
    >>> y_intercept(point, vector)
    -1.0

    """
    x1, x2 = point
    p1, p2 = vector

    return x2 - (x1 / p1) * p2

def max_points_on_line(X, p):
    """Compute the maximum number of points in X that fall on any line parallel to p.

    Parameters
    ----------
    X
        A list of 2-tuples containing integers.
    p
        A point as a 2-tuple of integers.

    Returns
    -------
    int

    Example
    -------

    >>> X = [
    ... (1, 1),
    ... (3, 1),
    ... (5, 2),
    ... (3, 6),
    ... (1, 7),
    ... (7, 4),
    ... (9, 3),
    ... (9, 9)
    ... ]
    >>> p = (-2, 1)
    >>> max_points_on_line(X, p)
    4

    """
    # counts_by_1_intersect is a dictionary whose keys are slopes and whose values are counts
    # of the times we see a point in X on the line with p with the given y-intersect. 
    # for the corner case where the slope is infinite (ie p[0] == 0), 
    # we use the x coordinate of the point as the key (which is the x-intersect of the line)

    counts_by_y_intersect = {}

    for x in X:
        if p[0] == 0:
            y_intersect = x[0] # actually the x-intersect
        else:
            y_intersect = compute_y_intercept(x, p)

        # Initialize the count for this slope if we haven't seen it before
        if y_intersect not in counts_by_y_intersect:
            counts_by_y_intersect[y_intersect] = 0

        # Update the count for this slope
        counts_by_y_intersect[y_intersect] = counts_by_y_intersect[y_intersect] + 1

    # the result is the maximum count of any line that passes through at least one point in X
    return max(counts_by_y_intersect.values()) 

