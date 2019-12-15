"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/

"""

# Drawing a triangle

import numpy as np
import cv2

height = 640
width = 840
color = (127, 127, 0)
image = np.zeros((height, width, 3), np.uint8)

print("Drawing a triangle")
print('The window size is {}X{}. Please enter a value by considering the size.'.format(width, height))
t = input("Please enter the length of the edge: ")
(x, y) = [x.strip("() ") for x in input("Please enter the starting point (x, y) format: ").split(",")]
t, x, y = int(t), int(x), int(y)

cv2.imshow("image", image)
cv2.waitKey(0)

for j in range(y, y +t+1):
    for i in range(x, x+y+t-j+1):
        image[i, j] = color
        
cv2.imshow("triangle image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()