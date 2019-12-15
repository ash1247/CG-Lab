"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/
Date: 11.10.2019 (DD.MM.YYYY)

"""

# Identifies a point whether it lies left or right
# side of a line

import cv2
import numpy as np

height = 640
width = 840
image = np.zeros((height, width, 3), np.uint8)

# Subtracted from height to fix the y axis
x0, y0 = 200, height-10 # Initial axes value of the line
x1, y1 = 500, height-600 # final axes value of the line
x2, y2 = 100, height-100 # The point axes value

cv2.line(image, (x0, y0), (x1, y1), (127, 127, 0), 5)
cv2.circle(image, (x2, y2), 3, (0, 0, 255), -1)
value = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)

if (value > 0):
    print("Left side of the line.")
elif (value < 0):
    print("Right side of the line.")
else:
    print("On the line")

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


