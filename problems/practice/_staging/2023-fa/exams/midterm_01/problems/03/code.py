def boo(n):
    for i in range(200, n):
        for j in range(i, i * n):
            print(i + j)

boo(202)
