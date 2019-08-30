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
from scipy.fftpack import fft
import matplotlib
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
left_channel = audio_data[:, 0]
right_channel = audio_data[:, 1]

# data values = amplitude of the wave (audio loudness)
# energy of the audio signal
# http://myinspirationinformation.com/uncategorized/audio-signals-in-python/
energy = np.sum(left_channel.astype(float)**2)
print("Energy: {}".format(energy))

# power of the audio signal
# power = energy per unit of time i.e. energy per second
power = 1.0 / (2*left_channel.size + 1) * energy / rate
print("Power: {}".format(power))

"""
# plot the track
time = np.arange(0, float(audio_data.shape[0]), 1) / rate

# plot amplitude over time
plt.plot(time, left_channel)
plt.show()
"""

# FFT
print(matplotlib.rcParams["agg.path.chunksize"])
matplotlib.rcParams["agg.path.chunksize"] = 10000
print(matplotlib.rcParams["agg.path.chunksize"])
fft_data = fft(audio_data[:, 0])
abs_fft_data = np.abs(fft_data)
plt.plot(audio_data, abs_fft_data)
plt.show()
