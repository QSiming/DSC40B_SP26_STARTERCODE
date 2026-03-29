def foo(n):
    i = 1
    while i < n**3:
        i = i * 2
        for j in range(n):
            print(i + j)
