"""
author: Ashikul Hosen
email: sagor.ashikul@gmail.com
github: https://github.com/ash1247/

"""

# Check Schaum's Computer Graphics 2nd Edition page 81 to understand this
# I just changed the values because opencv doesn't support negative
# pixel values

import numpy as np 
import math
import cv2

height = 640
width = 840
image = np.zeros((height, width, 3), np.uint8)

print("Scaling a triangle twice it's size keeping C point intact")
print('The window size is {}X{}. Please enter a value by considering the size.'.format(width, height))

# triangle point values stored in an 3x3 matrix
t_v = np.array([[1, 0, 550], # x
                [0, 1, 520], # y
                [0, 0, 1]])  # to complete square matrix
# scaling identity matrix 
s_2_2 = np.array([[2, 0, 0], # a, 0, 0
                  [0, 2, 0], # 0, b, 0
                  [0, 0, 1]]) # 0, 0, c
# stores triangle matrix that contains negative value 
# of the unchanged point 
t_neg_v = np.array([[1, 0, -550],
                    [0, 1, -520],
                    [0, 0, 1]])
# contains original points of the triangle
abc = np.array([[300, 410, 550], # x1 x2 x3
                [300, 410, 520], # y1 y2 y3
                [1, 1, 1]])      # to complete square matrix

s_2_2_c = (t_v.dot(s_2_2)).dot(t_neg_v)  # multiplies the matrices
print(s_2_2_c)

a1b1c1 = s_2_2_c.dot(abc) # contains the final unchanged values
print(a1b1c1)
print(a1b1c1[0][0])

cv2.line(image, (0, 0), (0, height), (255,0,0), 5)
cv2.line(image, (0, height), (width, height), (255,0,0), 5)

cv2.line(image, (300, height-300), (410, height-410), (0,0,255), 1)
cv2.line(image, (410, height-410), (550, height-520), (0,0,255), 1)
cv2.line(image, (550, height-520), (300, height-300), (0,0,255), 1)

cv2.imshow("image", image)
cv2.waitKey(0)

cv2.line(image, (300, height-300), (410, height-410), (0,0,0), 1)
cv2.line(image, (410, height-410), (550, height-520), (0,0,0), 1)
cv2.line(image, (550, height-520), (300, height-300), (0,0,0), 1)

cv2.line(image, (a1b1c1[0][0], height-a1b1c1[1][0]), (a1b1c1[0][1], height-a1b1c1[1][1]), (0,0,255), 1)
cv2.line(image, (a1b1c1[0][1], height-a1b1c1[1][1]), (a1b1c1[0][2], height-a1b1c1[1][2]), (0,0,255), 1)
cv2.line(image, (a1b1c1[0][2], height-a1b1c1[1][2]), (a1b1c1[0][0], height-a1b1c1[1][0]), (0,0,255), 1)

cv2.imshow("after image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
