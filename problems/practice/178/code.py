def boo(n):
    if n <= 1:
        return

    for i in range(3):
        boo(n/4)

    for j in range(n):
        print(j)
