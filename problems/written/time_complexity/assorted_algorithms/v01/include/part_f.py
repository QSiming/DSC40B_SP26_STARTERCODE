def f_6(n):
    for i in range(3*n + 5, n**2 + 3*n + 100):
        for j in range(int(n**0.5)):
            print(i, j)
