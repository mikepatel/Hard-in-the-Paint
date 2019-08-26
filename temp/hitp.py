"""
Michael Patel
May 2019
Python 3.6.5

Project Description:
    Create an animation over mp3 audio file

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
import pydub
import scipy.io.wavfile
import matplotlib.pyplot as plt


################################################################################
"""
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
################################################################################
# Analyze basic audio signals first
# "get a feel for audio data"

# convert music to data
# mp3 --> wav --> data array

# Read in mp3
mp3_filename = "treasure.mp3"
mp3_filename = os.path.join(os.getcwd(), mp3_filename)
mp3 = pydub.AudioSegment.from_mp3(mp3_filename)

# Convert mp3 to wav and Save wav file
mp3.export(os.path.join(os.getcwd(), "temp.wav"), format="wav")

# Read in wav file
rate, audio_data = scipy.io.wavfile.read(os.path.join(os.getcwd(), "temp.wav"))
print("Rate: {}".format(rate))
print("Wav audio data: {}".format(audio_data))

# Get track length
track_length = audio_data.shape[0] / rate
print("Track length: {:.4f}s".format(track_length))

# Get number of channels
num_channels = audio_data.shape[1]
print("Number of channels: {}".format(num_channels))


