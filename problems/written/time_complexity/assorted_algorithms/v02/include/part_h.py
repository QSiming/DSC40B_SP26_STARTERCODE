def f_8(n):
    i = 10
    while i < n**3:
        j = 0
        while j < i:
            j += 2
            print(i, j)
        i += 1
