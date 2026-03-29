def pairs(numbers):
    result = []
    for x in numbers:
        for y in numbers:
            result.append((x, y))
    return result
