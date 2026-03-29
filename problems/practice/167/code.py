def boo(first_list, second_list):
    """first_list and second_list are both of size n"""
    n = len(first_list)
    for x in second_list:
        count = 0
        for y in first_list:
            if x == y:
                count += 1
            if count >= n // 2:
                return True
    return False


print(boo([1, 6, 6, 4, 6], [6, 7, 8, 9, 10]))
