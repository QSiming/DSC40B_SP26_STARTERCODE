def f_1(n):
    total = 0
    for i in range(n**2):
        for j in range(n**2 + 5*n - 100):
            for k in range(n // 1_000_000):
                total += i**2 + n**2
    return total
