"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/
Date: 11.10.2019 (DD.MM.YYYY)

"""

# Implements the point clipping algorithm

import cv2 
import numpy as np

height = 640
width = 840
x_min, y_min = 200, height-200 # Initial axes value of the diagonal of the rectangle
x_max, y_max = 600, height-400 # final axes value of the diagonal of the rectangle
points = [(100, height-100), (250, height-250), (300, height-300), (350, height-350), (500, height-500),
            (150, height-150), (220, height-250), (500, height-450), (200, height-500)]


image = np.zeros((height, width, 3), np.uint8)

for i in points:
    cv2.circle(image, i, 5, (0, 0, 255), -1)

cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (127, 127, 0), 2)
cv2.imshow("Before point cliping", image)
cv2.waitKey(0)

for i in points:
    print(i)
    # The if condition for i[1] changed because of the vertical axis shift
    if (((i[0] < x_min) or (i[0] > x_max)) or ((i[1] > y_min) or (i[1] < y_max))):
        cv2.circle(image, i, 5, (0, 0, 0), -1)

cv2.imshow("After point clipping", image)
cv2.waitKey(0)
cv2.destroyAllWindows()