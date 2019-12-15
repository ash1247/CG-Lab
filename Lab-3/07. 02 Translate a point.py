"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/

"""

import numpy as np 
import cv2

height = 640
width = 840
image = np.zeros((height, width, 3), np.uint8)

print("Translating a point P to a new point P1")
print('The window size is {}X{}. Please enter a value by considering the size.'.format(width, height))
(x, y) = [x.strip("() ") for x in input("Please enter a point in (x, y) format: ").split(",")]
(x1, y1) = [x.strip("() ") for x in input("Please enter the new point in (x, y) format: ").split(",")]
x, y, x1, y1 = int(x), int(y), int(x1), int(y1)

cv2.line(image, (0, 0), (0, height), (255,0,0), 5)
cv2.line(image, (0, height), (width, height), (255,0,0), 5)

cv2.circle(image, (x, height-y), 4, (10,10,255), -1)
cv2.imshow("image", image)
cv2.waitKey(0)

cv2.circle(image, (x, height-y), 4, (0,0,0), -1)
cv2.circle(image, (x1, height-y1), 4, (10,10,255), -1)
cv2.imshow("after image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()