"""
Michael Patel
May 2019
Python 3.6.5

File Description:
    Create an animation over mp4 audio file

Notes:
    - gif => imagemagick
    - mp4 => ffmpeg
    - https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
    - https://github.com/jiaaro/pydub
    - https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html

"""

################################################################################
# Imports
import os
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


################################################################################
filename = "treasure" + ".mp3"
input_file = os.path.join(os.getcwd(), filename)
print(input_file)

sound = AudioSegment.from_mp3(input_file)
samples = sound.get_array_of_samples()
samples = np.array(samples)
print(len(np.shape(samples)))  # check how many channels
#print(samples)
plt.plot(samples)
plt.show()
#play(sound)

"""
fig, ax = plt.subplots()
x = []
y = []
ln, = plt.plot([], [], animated=True)
f = np.linspace(-3, 3, 200)


def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.25, 2)
    ln.set_data(x, y)
    return ln,


def update(frame):
    x.append(frame)
    y.append(np.exp(-frame*2.0))
    ln.set_data(x, y)
    return ln,


anim = FuncAnimation(fig, update, frames=f, init_func=init, interval=2.5, blit=True, repeat=False)
plt.show()
"""





