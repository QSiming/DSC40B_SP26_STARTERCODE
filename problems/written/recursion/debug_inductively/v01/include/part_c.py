def inplace_reverse(l, start, stop):
    """After running this, l[start:stop] should be reversed."""
    if stop - start <= 1:
        return
    l[start], l[stop-1] = l[stop-1], l[start] # swap first and last
    inplace_reverse(l, start, stop-1)
