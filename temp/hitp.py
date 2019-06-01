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

"""

################################################################################
# Imports
import os
import cv2
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt


################################################################################
filename = "treasure" + ".mp3"
input_file = os.path.join(os.getcwd(), filename)
print(input_file)

"""
# create VideoCapture object by reading from video file
vc = cv2.VideoCapture(input_file)

while vc.isOpened():
    ret, frame = vc.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vc.release()
cv2.destroyAllWindows()
"""
#playsound(input_file)
sound = AudioSegment.from_mp3(input_file)
samples = sound.get_array_of_samples()
print(type(samples))
#print(samples)
plt.plot(samples)
plt.show()
play(sound)

