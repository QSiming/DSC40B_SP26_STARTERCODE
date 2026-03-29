def slow_histogram(points, bins):
    """This is a solution that has the incorrect time complexity."""
    result = []
    n = len(points)

    for bin_start, bin_end in bins:
        bin_count = 0
        for point in points:
            if bin_start <= point < bin_end:
                bin_count += 1
        result.append(bin_count / (n * (bin_end - bin_start)))

    return result
