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

# Put pixel for each step
x = x1
y = y1

# calculate dx , dy, dt, ds and d
dx = x2 - x1
dy = y2 - y1
dt = 2 * (dy-dx)
ds = 2 * dy
d = ds - dx

image[int(x), int(y)] = color
# colors the pixels
while(x < x2):
    x += 1
    if (d < 0):
        d = d + ds
    else:
        y += 1
        d = d + dt
    image[int(x), int(y)] = color

cv2.imshow("Line Algorithm Bresenham", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
