def max_points_on_line(X, p):
    """Compute the maximum number of points in X that fall on any line that includes p.

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
    >>> p = (5, 5)
    >>> max_points_on_line(X, p)
    4

    """
    # counts_by_slope is a dictionary whose keys are slopes and whose values are counts
    # of the times we see a point in X on the line with p with the given slope. By
    # convention, two distinct points on the same line will have a slope of infinity,
    # and two identical points will have a slope of None
    #
    # we'll initialize the dictionary with a key of None because we will be counting the
    # number of points in X that are identical to the query point p in order to handle
    # that corner case; see the comment above the return statement below for more info.
    counts_by_slope = {None: 0}

    maximum = 0

    for x in X:
        m = slope_between(x, p)

        # Count of points equivalent to p
        if m is None:
            counts_by_slope[None] += 1
            continue

        # Initialize the count for this slope if we haven't seen it before
        if m not in counts_by_slope:
            counts_by_slope[m] = 0

        # Update the count for this slope
        count = counts_by_slope[m] = counts_by_slope[m] + 1

        if count > maximum:
            maximum = count

    # if a point in X equals the query point p, it is automatically on any line
    # containing p, but it wasn't counted by the code above. Instead, it was counted in
    # counts_by_slope[None], thus we add it here
    return maximum + counts_by_slope[None]


def slope_between(p, q):
    """Computes the slope between 2 dimensional points, p and q.

    If p and q are on the same vertical line, we adopt the convention that the
    slope between them is infinity. However, if p and q are identical, we'll
    return None so that we can distinguish this corner case.

    """

    p_x, p_y = p
    q_x, q_y = q

    dx = q_x - p_x
    dy = q_y - p_y

    if dx == 0 and dy == 0:
        return None

    if dx == 0:
        return float("inf")

    return dy / dx
