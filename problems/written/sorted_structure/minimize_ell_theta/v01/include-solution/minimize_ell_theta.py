def minimize_ell_sorted(data, color):
    n = len(data)
    min_theta = data[0]
    min_loss = float('inf')
    red_seen = 0
    blue_seen = 0
    for i in range(len(data)):
        if color[i] == "red":
            red_seen += 1
        elif color[i] == "blue":
            blue_seen += 1
        blue_not_seen = n/2 - blue_seen
        loss = red_seen + blue_not_seen
        if loss < min_loss:
            min_loss = loss
            min_theta = data[i]
    return min_theta
