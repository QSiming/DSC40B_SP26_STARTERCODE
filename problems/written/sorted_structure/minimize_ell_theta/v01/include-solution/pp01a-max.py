def learn_theta(data, colors):
    # return the largest blue point
    blue_points = (x for x, c in zip(data, colors) if c == 'blue')
    return max(blue_points)
