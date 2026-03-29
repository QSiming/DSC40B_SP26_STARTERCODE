import numpy as np
import matplotlib.pyplot as plt

points = [1, 2, 3, 6, 7, 9, 10, 11]
bins = [0, 4, 8, 12]

plt.hist(points, bins=bins, density=True)
plt.savefig('../include/histogram.png')
