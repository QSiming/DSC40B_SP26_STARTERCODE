def f(n):
    i = 1
    while i <= n:
        i *= 3
        for j in range(i):
            print(i, j)
