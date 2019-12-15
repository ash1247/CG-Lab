"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/

"""

# reset the 24-bit 256-entry lookup table
# to it's complementary color

import numpy as np
import cv2

image = cv2.imread("./05. 2.35.png")
cv2.imshow("image", image)
cv2.waitKey(0)

lookup_table = {}
for i in range(0, 256):
    for j in range(0, 550):
        lookup_table[i] = image[i, j]
        b, g, r = lookup_table[i]
        lookup_table[i] = 255-b, 255-g, 255-r
        image[i, j] = lookup_table[i]
    
cv2.imshow("after switch image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()