# Simple thresholding and Adaptive thresholding

import cv2

img = cv2.imread('../Resources/images/cats.jpg')
cv2.imshow('Image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)

#Simple thresholding
# here 150 is the threshold, if the pixel value is less than 150 than it is set to 0 or else to 255
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('THRESHOLD', thresh)

threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('THRESHOLD_INVERSE', thresh_inv)

# Adaptive thresholding (Opencv learns by itself, no manual input of value)
Adapt = cv2.adaptiveThreshold(gray, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          thresholdType=cv2.THRESH_BINARY, blockSize= 15, C= 35 )
cv2.imshow("Adaptive thresh", Adapt)

cv2.waitKey(0)