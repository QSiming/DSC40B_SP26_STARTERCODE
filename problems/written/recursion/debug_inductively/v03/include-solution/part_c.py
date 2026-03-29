def inplace_reverse(l, start, stop):
    """Reverses l[start:stop], in place."""
    if stop - start <= 1:
        return
    l[start], l[stop-1] = l[stop-1], l[start] # swap first and last
    inplace_reverse(l, start+1, stop-1)
