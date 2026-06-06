def learn_theta(data, colors):
    '''
    Finds theta that is larger than all blue and less than all red.
    '''
    # TODO: Implement the learn_theta function
    
    theta = None

    for x, color in zip(data, colors):
        if color == 'blue':
            if theta is None or x > theta:
                theta = x

    return float(theta)


def compute_ell(data, colors, theta):
    '''
    Computes the loss function L(theta) for a given theta.
    '''
    # TODO: Implement the compute_ell function
    
    loss = 0

    for x, color in zip(data, colors):
        if color == 'red' and x <= theta:
            loss += 1
        elif color == 'blue' and x > theta:
            loss += 1

    return float(loss)


def minimize_ell(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) using quadratic time complexity.
    '''
    # TODO: Implement the minimize_ell function
    
    best_theta = data[0]
    best_loss = compute_ell(data, colors, best_theta)

    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return float(best_theta)


def minimize_ell_sorted(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) in linear time.
    '''
    # TODO: Implement the minimize_ell_sorted function
    blue_gt_theta = sum(1 for color in colors if color == 'blue')
    red_le_theta = 0

    best_theta = data[0]
    best_loss = float('inf')

    for i in range(len(data)):
        # Now move theta to data[i]. Update the two counts.
        if colors[i] == 'blue':
            blue_gt_theta -= 1
        else:
            red_le_theta += 1

        loss = red_le_theta + blue_gt_theta

        if loss < best_loss:
            best_loss = loss
            best_theta = data[i]

    return float(best_theta)

