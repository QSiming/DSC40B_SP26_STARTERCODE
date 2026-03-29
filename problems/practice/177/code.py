import random
import math

def boo(n):
    # draw a number uniformly at random from 0, 1, 2, ..., n-1 in Theta(1)
    x = random.randrange(n)

    if x < math.log2(n):
        for i in range(n**2):
            print("Very unlucky!")
    elif x < math.sqrt(n):
        for i in range(n):
            print("Unlucky!")
    else:
        print("Lucky!")

boo(100)
