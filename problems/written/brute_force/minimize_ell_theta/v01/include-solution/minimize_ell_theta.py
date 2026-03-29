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
