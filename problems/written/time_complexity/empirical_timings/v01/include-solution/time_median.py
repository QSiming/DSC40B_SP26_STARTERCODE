def time_median(n):
    # it's also valid to produce any other list with length n
    lst = [random.random() for _ in range(n)]
    elapses = []
    for _ in range(10):
        start = time.time()
        med = median(lst)
        end = time.time()
        elapses.append(end - start)
    return sum(elapses)/10