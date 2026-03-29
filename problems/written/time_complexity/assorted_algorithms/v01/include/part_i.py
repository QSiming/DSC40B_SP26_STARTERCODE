def f_9(n):
    for x in range(3*n + 1_000_000, 5*n):
        for y in range(42):
            print(x, y)
