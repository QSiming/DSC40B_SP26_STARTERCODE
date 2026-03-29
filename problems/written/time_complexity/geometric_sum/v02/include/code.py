def f(n):
    i = 1
    while i <= n:
        i *= 2
        for j in range(i**2): # <-- note the range!
            print(i, j)
