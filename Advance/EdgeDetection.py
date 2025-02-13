# Edge detection using the laplacian, sobel and canny


import cv2
import numpy as np

img = cv2.imread('../Resources/images/my_photo.jpg')
cv2.imshow('Image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY', gray)

# Laplacian
lap = cv2.Laplacian(gray, ddepth=cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplace", lap)

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
cv2.imshow("Sobelx", sobelx)

sobely = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
cv2.imshow("Sobely", sobely)

mergedSobel = cv2.bitwise_or(sobelx, sobely)
cv2.imshow("Merged", mergedSobel)

#CANNY
canny = cv2.Canny(gray, 150, 175)
cv2.imshow("CANNY", canny)
cv2.waitKey(0)
