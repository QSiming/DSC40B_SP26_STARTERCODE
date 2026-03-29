def f_8(n):
i = 10
while i < n**2:
    i += 3
    for j in range(n):
        print(i, j)
