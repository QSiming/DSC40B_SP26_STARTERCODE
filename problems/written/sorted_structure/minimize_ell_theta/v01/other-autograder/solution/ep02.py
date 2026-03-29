def learn_theta(data, colors):
    biggest_blue = -float('inf')
    for x, color in zip(data, colors):
        if color == 'blue' and x > biggest_blue:
            biggest_blue = x
    return biggest_blue


def compute_ell(data, colors, theta):
    loss = 0
    for x, color in zip(data, colors):
        if (color == 'red' and x <= theta) or (color == 'blue' and x > theta):
            loss += 1
    return loss


def minimize_ell(data, colors):
    minimum_loss = float('inf')
    minimum_theta = None
    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < minimum_loss:
            minimum_loss = loss
            minimum_theta = theta
    return minimum_theta
