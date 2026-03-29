sizes = [1_000, 10_000, 100_000, 1_000_000]

MS_IN_S = 1_000_000
MS_IN_M = MS_IN_S * 60
MS_IN_H = MS_IN_M * 60
MS_IN_D = MS_IN_H * 24
MS_IN_Y = MS_IN_D * 365

MS_IN = {
    'years': MS_IN_Y,
    'days': MS_IN_D,
    'hours': MS_IN_H,
    'minutes': MS_IN_M,
    'seconds': MS_IN_S,
}

def time_taken(f):
    return [humanize(f(s)) for s in sizes]

def humanize(ms):
    for unit, amount in MS_IN.items():
        if ms / amount >= 1:
            return f'{ms / amount:0.2f} {unit}'
    return f'{ms / amount:0.2f} {unit}'

# linear time
time_taken(lambda: n)

# quadratic
time_taken(lambda: n**2)

# cubic
time_taken(lambda: n**3)
