import random
def foo(n):
    # draw a number uniformly at random from 0, 1, 2, ..., n-1 in Theta(1) time
    x = random.randrange(n)
    if x < 20:
        for i in range(n**3):
            print("Very unlucky!")
    elif x < n / 2:
        for i in range(n):
            print("Unlucky!")
    else:
        print("Lucky!")
