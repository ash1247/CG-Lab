import numpy as np
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc

width = 1280
height = 720
FPS = 240
points = 1000
color = (127, 127, 127) # gray

radius = int(input("Please enter the radius of the circle: "))

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# Returns evenly spaced numbers over a specified interval.
t = np.linspace(0, 2*np.pi, points+1)
# creates x value of the given t value
x = radius * np.cos(t)
# creates y value of the given t value
y = radius * np.sin(t)

# descibes the fourcc codec type
fourcc = VideoWriter_fourcc(*'MP42')
#writes video in the given filename and codec. Animation speed depends on FPS.
video = VideoWriter('./circle_animation.mkv', fourcc, float(FPS), (width, height))

# creates a colored frame
frame = np.zeros((height, width, 3), dtype=np.uint8)

# colors the given pixels of the frame by looping and writes the frame in video
for xi, yi in np.c_[x, y]:
    frame[int((xi)+(height/2)), int((yi)+(width/2))] = color
    video.write(frame)

video.release()

# trtl.color('red', 'green')
# trtl.pensize(5)
# trtl.circle(radius, 360, 100)

# trtl.done()

