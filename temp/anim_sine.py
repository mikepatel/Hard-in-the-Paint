"""
Michael Patel
May 2019
Python 3.6.5

File Description:
    A tutorial to create a basic animation of a moving sine wave using Matplotlib animation

Notes:
    - gif => imagemagick
    - mp4 => ffmpeg
    - https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c

"""

################################################################################
# Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


################################################################################
plt.style.use("dark_background")
fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=3)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01*i))
    line.set_data(x, y)
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=200, interval=20, blit=True)

print("Saving gif...")
anim.save("sine_wave.gif", writer="imagemagick")
