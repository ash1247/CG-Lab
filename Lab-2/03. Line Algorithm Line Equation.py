import numpy as np
import cv2

width = 1440
height = 720
points = 300
color = (127, 127, 127) # gray

m = int(input("Please enter the slope of the line: "))
b = int(input("Please enter the y-intercept of the line: "))

# numpy.arange([start, ]stop, [step, ]dtype=None)
# Return evenly spaced values within a given interval.
x = np.arange(0, points, 1)
# line equation, m = slope, b = y-intercept
y = m * x + b

# creates a colored frame
image = np.zeros((height, width, 3), dtype=np.uint8)

# colors the given pixels of the frame by looping
for xi, yi in np.c_[x, y]:
    image[int(xi)+10, int(yi)+20] = color

cv2.imshow("Line Algorithm Line Equation",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
