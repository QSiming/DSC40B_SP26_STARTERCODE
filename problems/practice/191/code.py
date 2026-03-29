def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[j]:
            return False
    return True


def foo(list1, list2):
    if are_lists_equal(list1, list2):
        for i in list1:
            print(i)
    else:
        for i in list1:
            for j in list2:
                for k in range(len(list1)):
                    print(i, j, k)
