import random

def foo(arr):
    n = len(arr)
    x = random.randrange(0, n)
    if x < n // 3:
        return sum(arr)
    else:
        return 0


print(foo([1,2,3,4]))
