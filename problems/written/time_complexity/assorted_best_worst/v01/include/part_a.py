def f_1(data):
    """`data` is a two-dimensional array of size n*n"""
    n = len(data)
    for i in range(n):
        for j in range(n):
            if data[i, j] == 42:
                return (i,j)
