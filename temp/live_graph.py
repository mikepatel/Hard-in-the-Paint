"""
Michael Patel
May 2019
Python 3.6.5

File Description:
    A tutorial to create a live graph using Matplotlib animation

Notes:
    - gif => imagemagick
    - mp4 => ffmpeg

"""

################################################################################
# Imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

# create subplot
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    data = open("data.txt", "r").read()
    lines = data.split("\n")
    xs = []
    ys = []

    for line in lines:
        x, y = line.split(",")
        xs.append(float(x))
        ys.append(float(y))

    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Live Graph with Matplotlib")


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
