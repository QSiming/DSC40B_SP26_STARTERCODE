sizes = [100, 400, 700, 1000, 1300, 1600, 1900]
timings = []
for s in sizes:
    timings.append(time_median(s))
plt.plot(sizes, timings)
plt.xlabel('Input Size')
plt.ylabel('Average Time Taken')
plt.title('Average Time For Finding Median')
