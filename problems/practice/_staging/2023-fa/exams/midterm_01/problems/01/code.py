import math
def boo(n):
    for i in range(n):
        for j in range(n**2 + 100, 500*n**3):
            for k in range(1_000, math.floor(math.log(n))):
                print(i + j + k)

boo(100)
