def f_2(data):
    """`data` is an array of n numbers"""
    n = len(numbers)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,n):
            if numbers[i-1] < numbers[i]:
                # next line swaps elements in Theta(1) time
                numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
                swapped = True
