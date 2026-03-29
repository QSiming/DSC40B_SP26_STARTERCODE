def redemption_value(n):
    """Helper function returning the value of a token, if it is redeemed.

    Parameters
    ----------
    n : int
        What number of token is this? If n = 1, this is the first token being redeemed.
        If n = 2, it is the second, and so on.

    """
    values = {
        1: 50,
        2: 30,
        3: 20
    }
    # return the value from the dictionary, and 10 otherwise. This is because
    # all tokens from the fourth token redeemed on are worth 10 points of extra
    # credit
    return values.get(n, 10)

def allocate_tokens(late, n_tokens):
    # sort from largest to smallest
    late = sorted(late, reverse=True)

    total_points = 0
    number_of_tokens_used_for_ec = 0
    late_ix = 0 # index of the late being considered

    # loop while there are lates and tokens left
    while late_ix < len(late) and n_tokens > 0:
        # the number of points we'd earn if we redeem the token
        extra_credit = redemption_value(number_of_tokens_used_for_ec + 1)

        # the number of points that would be earned by "flipping" the late assignment
        late_points = late[late_ix]

        if extra_credit > late_points:
            # redeem the token for extra credit
            total_points += extra_credit
            number_of_tokens_used_for_ec += 1
        else:
            # use the token to "flip" the homework to on-time
            total_points += late_points
            # move on to the next homework
            late_ix += 1

        # either way, we used a token
        n_tokens -= 1

    # if there are still tokens remaining, use all of them for extra credit
    for i in range(n_tokens):
        total_points += redemption_value(number_of_tokens_used_for_ec + 1)
        number_of_tokens_used_for_ec += 1

    return total_points
