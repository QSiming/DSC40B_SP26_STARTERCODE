def f_10(n):
    i = 1
    while i <= n:
        i *= 2
        for j in range(i):
            print(i, j)
