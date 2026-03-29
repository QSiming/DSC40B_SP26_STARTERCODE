def f_1(n):
    for i in range(1_000_000, n):
        for j in range(i):
            print(i, j)
