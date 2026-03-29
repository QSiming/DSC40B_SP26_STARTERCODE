def f_2(n):
    total = 0
    for i in range(n):
        for j in range(5*n):
            for k in range(n - j):
                total += i + j + k
    return total
