"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/

"""

# initialize a 24 bit 256-entry lookuptable with gray-scale value
# lookup_table is a color matrix that stores rgb or in this case
# bgr values

import numpy as np
import cv2

y = 256
x = 384

image = np.zeros((y, x, 3), np.uint8)

cv2.imshow("image", image)
cv2.waitKey(0)

lookup_table = {}
for i in range(0, 256):
    lookup_table[i] = 127
    image[i] = 127

cv2.imshow("Look up table image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(lookup_table)