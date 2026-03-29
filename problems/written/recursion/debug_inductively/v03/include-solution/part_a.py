def reverse(s):
    """Reverse a string."""
    if not s: # if s is empty...
        return "" # return the empty string
    return reverse(s[1:]) + s[0]
