import numpy as np
import cv2

width = 1440
height = 720
color = (127, 127, 127) # gray

print('The window size is {}X{}. Please enter a value by considering the size.'.format(height, width))
(x1, y1) = [x.strip("() ") for x in input("Please enter a point in (x, y) format for the starting vertex: ").split(",")]
(x2, y2) = [x.strip("() ") for x in input("Please enter a point in (x, y) format for the opposite vertex: ").split(",")]
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

# creates a colored frame
image = np.zeros((height, width, 3), dtype=np.uint8)

# calculate dx , dy
dx = x2 - x1
dy = y2 - y1

# Depending upon absolute value of dx & dy
# choose number of steps to put pixel as steps
steps = abs(dx) if (abs(dx) > abs(dy)) else abs(dy)

# calculate increment in x & y for each steps
x_inc = dx / steps
y_inc = dy / steps

# Put pixel for each step
x = x1
y = y1

# colors the given pixels of the frame by looping 
for index in range(steps+1):
    image[int(x), int(y)] = color
    x += x_inc
    y += y_inc

cv2.imshow("Line Algorithm DDA",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
