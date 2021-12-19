import numpy as np
import matplotlib.pyplot as plt


def number_of_lines(fail_name):
    f = open(fail_name, 'r')
    n = 0
    while True:
        line = f.readline()
        if not line:
            break
        n += 1
    f.close()
    return n


n = number_of_lines('frames.txt')
f = open('frames.txt', 'r')
for k in range((n // 2)):
    X = []
    Y = []
    line = f.readline()
    for i in line.split():
        X.append(float(i))
    line1 = f.readline()
    for j in line1.split():
        Y.append(float(j))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Major ticks every 20, minor ticks every 5
    major_ticks_X = np.arange(0, 16, 1)
    minor_ticks_X = np.arange(0, 16, 0.5)
    major_ticks_Y = np.arange(-9, 12, 1)
    minor_ticks_Y = np.arange(-9, 12, 0.5)

    ax.set_xticks(major_ticks_X)
    ax.set_xticks(minor_ticks_X, minor=True)
    ax.set_yticks(major_ticks_Y)
    ax.set_yticks(minor_ticks_Y, minor=True)

    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    ax.set_title('Frame' + str(k))
    plt.axis([0, 16, -9, 12])
    plt.plot(X, Y)
    plt.grid(True)
    plt.savefig('Frame' + str(k) + '.png')
f.close()