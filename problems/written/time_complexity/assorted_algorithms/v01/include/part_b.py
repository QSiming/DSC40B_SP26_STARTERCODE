def f_2(n):
    total = 0
    for i in range(n):
        for j in range(n + i):
            total += max(i, j)
    return total
