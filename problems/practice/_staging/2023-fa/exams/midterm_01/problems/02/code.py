import math

def boo(n):
    for i in range(n):
        for j in range(n):
            print(i + j)

    for i in range(math.floor(math.sqrt(n))):
        for j in range(math.log2(i), i * math.floor(math.log2(i + 10))):
            print(i + j)
