def foo(n):
    for i in range(n):
        for j in range(i**2):  # notice the bound!
            print(i + j)
