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

def minimize_ell_sorted(data, color):
    min_theta = data[0]
    min_loss = 100000
    for i in data:
        red = 0
        blue = 0
        for j in range(len(data)):
            if data[j] <= i and color[j] == "red":
                red += 1
            elif data[j] > i and color[j] == "blue":
                blue += 1
        if red + blue < min_loss:
            min_loss = red + blue
            min_theta = i
    return min_theta
