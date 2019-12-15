"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/

"""

# Drawing a rectangle

import numpy as np
import cv2

height = 640
width = 840
color = (127, 127, 0)
image = np.zeros((height, width, 3), np.uint8)

print("Drawing a rectangle")
print('The window size is {}X{}. Please enter a value by considering the size.'.format(width, height))
(w, h) = [x.strip("() ") for x in input("Please enter the area in (w, h) format: ").split(",")]
(x, y) = [x.strip("() ") for x in input("Please enter the starting point (x, y) format: ").split(",")]
w, h, x, y = int(w), int(h), int(x), int(y)

cv2.imshow("image", image)
cv2.waitKey(0)

for j in range(y, y + h):
    for i in range(x, x+w):
        image[i, j] = color
        
cv2.imshow("rectangle image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()