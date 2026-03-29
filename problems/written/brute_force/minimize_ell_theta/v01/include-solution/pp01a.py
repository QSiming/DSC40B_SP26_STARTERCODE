def learn_theta(data, colors):
    biggest_blue = -float('inf')
    for x, color in zip(data, colors):
        if color == 'blue' and x > biggest_blue:
            biggest_blue = x
    return biggest_blue
