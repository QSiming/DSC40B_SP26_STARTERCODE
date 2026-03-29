def f_5(n):
    ranges = [10, n//2, n, n**2]
    for rng in ranges:
        for i in range(rng):
            print(i)
