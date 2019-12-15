"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/

"""
# This program works best in the full axis
# This program only works in first quadrant

import numpy as np 
import math
import cv2

height = 640
width = 840
image = np.zeros((height, width, 3), np.uint8)

print("Rotating a point 45 degrees")
print('The window size is {}X{}. Please enter a value by considering the size.'.format(width, height))
(x, y) = [x.strip("() ") for x in input("Please enter a point in (x, y) format: ").split(",")]
x, y = int(x), int(y)
# r_thetha matrix stores this matrix
# cost -sint
# sint  cost
r_theta = np.array([[math.cos(math.radians(45)), -math.sin(math.radians(45))],
                [math.sin(math.radians(45)), math.cos(math.radians(45))]])
print(r_theta)
# new point values are stored in p1
p1 = r_theta.dot(np.array([[x], 
                          [y]]))
print(p1)
p1 = (int(p1[0][0]), int(p1[1][0]))
print(p1)


cv2.line(image, (0, 0), (0, height), (255,0,0), 5)
cv2.line(image, (0, height), (width, height), (255,0,0), 5)

cv2.circle(image, (x, height-y), 4, (10,10,255), -1)
cv2.imshow("image", image)
cv2.waitKey(0)

cv2.circle(image, (x, height-y), 4, (0,0,0), -1)
cv2.circle(image, p1, 4, (10,10,255), -1)
cv2.imshow("after image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()