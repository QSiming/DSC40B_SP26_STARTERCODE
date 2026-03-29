def count_execs_for_case(k):
    number_of_execs = 0

    for i in range(k):
        for j in range(i):
            print("Hello!")
            number_of_execs += 1

    return number_of_execs

print(count_execs_for_case(9))
