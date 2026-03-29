def f_5(n):
    ranges = [10, n//2, n, n**2]
    for rng_a in ranges:
        for rng_b in ranges:
            for i in range(rng_a + rng_b):
                print(i)
