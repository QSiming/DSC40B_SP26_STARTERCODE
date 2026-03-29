import math

def boo(n):
    i = n
    while i > 1:
        i = i / 2
        for j in range(1_000_000):
            print(i + j)

boo(100)
