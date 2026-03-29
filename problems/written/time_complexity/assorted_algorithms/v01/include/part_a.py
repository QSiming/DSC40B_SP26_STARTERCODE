def f_1(n):
    total = 0
    for i in range(n):
        for j in range(n**2):
            for k in range(n//4):
                total += max(i, j, k)
    return total
