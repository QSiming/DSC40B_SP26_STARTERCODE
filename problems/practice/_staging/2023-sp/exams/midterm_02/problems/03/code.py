def intersection(A, B):
    common = set()
    for x in A:
        if x in B:
            common.add(x)
    return common


A = {1, 3, 5, 7, 9}
B = {1, 5, 9, 12, 13}

print(intersection(A, B))
