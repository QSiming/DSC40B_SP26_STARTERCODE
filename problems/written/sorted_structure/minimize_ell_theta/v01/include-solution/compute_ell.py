def compute_ell(data, colors, theta):
    loss = 0
    for x, color in zip(data, colors):
        if (color == 'red' and x <= theta) or (color == 'blue' and x > theta):
            loss += 1
    return loss
