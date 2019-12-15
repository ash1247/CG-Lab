"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/
Date: 11.10.2019 (DD.MM.YYYY)

"""

# Identifies a point whether it lies inside
# or outside of a circle

import cv2
import math
import numpy as np

height = 640
width = 840
image = np.zeros((height, width, 3), np.uint8)

# Subtracted from height to fix the y axis
x0, y0 = 420, height-320 # The axes value of the center of the circle
x1, y1 = 120, height-320 # The point axes value
radius = 100

cv2.circle(image, (x0, y0), radius, (127, 127, 0), 2) # The main circle
cv2.circle(image, (x1, y1), 3, (0, 0, 255), -1) # The point is shown as a circle
value = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

if (value > radius):
    print("The point is outside the circle.")
elif (value < radius):
    print("The point is inside the circle.")
else:
    print("The point is on the circumference of the circle.")

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()