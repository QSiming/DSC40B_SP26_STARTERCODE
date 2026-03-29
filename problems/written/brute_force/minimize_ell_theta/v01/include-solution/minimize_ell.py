def minimize_ell(data, colors):
    minimum_loss = float('inf')
    minimum_theta = None
    for theta in data:
        loss = compute_ell(data, colors, theta)
        if loss < minimum_loss:
            minimum_loss = loss
            minimum_theta = theta
    return minimum_theta
