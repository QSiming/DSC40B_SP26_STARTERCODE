def f_1(arr1, arr2):
    """`arr1` and `arr2` are two arrays each of size n"""
    n = len(arr1)
    for i in range(n):
        for j in range(n):
            if arr1[i] + arr2[j] == 0:
                return (i, j)