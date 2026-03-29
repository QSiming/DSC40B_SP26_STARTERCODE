def balance(left, right):
    left_sum = sum(left)
    right_sum = sum(right)

    best_swap = (None, None)
    best_difference = float('inf')


    left_ix = 0
    right_ix = 0

    while left_ix < len(left) and right_ix < len(right):
        updated_left = left_sum + right[right_ix] - left[left_ix]
        updated_right = right_sum + left[left_ix] - right[right_ix]

        difference = updated_left - updated_right
        if abs(difference) < best_difference:
            best_swap = left_ix, right_ix
            best_difference = abs(difference)

        # the right side is too small
        if difference == 0:
            return (left_ix, right_ix)
        elif difference > 0:
            # if the right side is too small, then swapping the current left_ix
            # with anything to the right of the current right_ix would just make
            # things worse. This means that we can rule out left_ix and increment it.
            left_ix += 1
        else:
            right_ix += 1

    return best_swap


def brute_force(left, right):
    left_sum = sum(left)
    right_sum = sum(right)

    best_swap = (None, None)
    best_difference = float('inf')

    for left_ix in range(len(left)):
        for right_ix in range(len(right)):
            updated_left = left_sum + right[right_ix] - left[left_ix]
            updated_right = right_sum + left[left_ix] - right[right_ix]

            difference = updated_left - updated_right
            if abs(difference) < best_difference:
                best_swap = left_ix, right_ix
                best_difference = abs(difference)

            if difference == 0:
                return (left_ix, right_ix)

    return best_swap
