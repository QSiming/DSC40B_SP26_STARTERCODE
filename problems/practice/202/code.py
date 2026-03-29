def foo(n):
    if n <= 1:
        return

    foo(n // 2)

    for j in range(n):
        print(j)

    foo(n // 2)
