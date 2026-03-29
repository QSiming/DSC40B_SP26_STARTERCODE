import random

def boo(n):
    # draw a number uniformly at random from 0, 1, 2, ..., n-1 in Theta(1)
    x = random.randrange(n)

    for i in range(x): # <-- note that the range is random!
        print(i)
