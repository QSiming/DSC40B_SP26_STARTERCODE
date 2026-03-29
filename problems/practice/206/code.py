def foo(n):
    if n < 2023:
        bar_1(n**3)
    elif n == 2023:
        bar_3(n**2)
    else:
        bar_2(n)
