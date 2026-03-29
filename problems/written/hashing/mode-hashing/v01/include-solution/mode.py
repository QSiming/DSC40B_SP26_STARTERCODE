def mode(numbers):
    # keep track of counts in a dictionary
    counts = {}

    for number in numbers:
        if number not in counts:
            counts[number] = 1
        else:
            counts[number] += 1

    # this returns the dictionary key that has the largest value
    return max(counts, key=lambda key: counts[key])
