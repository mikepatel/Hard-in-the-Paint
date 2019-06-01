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

"""

################################################################################
# Imports
import os
import cv2
from playsound import playsound


################################################################################
input_file = os.path.join(os.getcwd(), "hitp.mp3")

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
playsound(input_file)
