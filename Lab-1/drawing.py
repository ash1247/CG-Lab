import numpy as np
import cv2

y = 640
x = 840

image = np.zeros((y, x, 3), np.uint8)

print('The window size is {}X{}. Please enter a value by considering the size.'.format(x, y))
(x1, y1) = [x.strip("() ") for x in input("Please enter a point in (x, y) format for the starting vertex: ").split(",")]
(x2, y2) = [x.strip("() ") for x in input("Please enter a point in (x, y) format for the opposite vertex: ").split(",")]
r = int(input("Please enter the radius of the circle: "))
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

# cv2.rectangle(image, (100, 100), (750, 400), color=(0,255,0), thickness=2)

# cv2.line(image, (100, 100), (750, 400), color=(200,12,127), thickness=2)
# cv2.line(image, (100, 400), (750, 100), color=(200,12,127), thickness=2)
# cv2.line(image, (425, 400), (425, 100), color=(200,12,127), thickness=2)
# cv2.line(image, (100, 250), (750, 250), color=(200,12,127), thickness=2)

cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)

cv2.line(image, (x1, y1), (x2, y2), (200,12,127), 2)
cv2.line(image, (x1, y2), (x2, y1), (200,12,127), 2)
cv2.line(image, (int((x1+x2)/2), y2), (int((x1+x2)/2), y1), (200,12,127), 2)
cv2.line(image, (x1, int((y1+y2)/2)), (x2, int((y1+y2)/2)), (200,12,127), 2)

# cv2.circle(image, (425, 250), 100, color=(10,10,255), thickness=2)
cv2.circle(image, (int((x1+x2)/2), int((y1+y2)/2)), r, (10,10,255), 2)


cv2.imshow("Rectangle Image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
