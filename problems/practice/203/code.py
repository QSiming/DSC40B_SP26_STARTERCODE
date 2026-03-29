import math
def foo(n):
    for i in range(3 * n**3 + 5 * n * math.ceil(math.log(n))):
        for j in range(math.floor(math.sqrt(n))):
            print(i + j)
        for k in range(n**2):
            print(k * i)
