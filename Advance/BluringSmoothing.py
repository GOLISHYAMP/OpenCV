# Types of Blurring is 
# Averaging, median, gaussian and bilateral

import cv2
import numpy as np

img = cv2.imread('../Resources/images/cats.jpg')
cv2.imshow('img', img)

#Average
avg = cv2.blur(img, (3,3))
cv2.imshow('AVG', avg)

# Median
median = cv2.medianBlur(img, 3)
cv2.imshow('median', median)

# Gaussian
guass = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow('guassian', guass)

#Bilateral
bilateral = cv2.bilateralFilter(img, 30, 50, 50)
cv2.imshow('bilateral', bilateral)

gray = cv2.cvtColor(bilateral, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# It just remove the pixel whose value are below 125
ret, thres = cv2.threshold(gray, thresh= 185, maxval=255, type= cv2.THRESH_BINARY)
cv2.imshow('threshold', thres)

print(gray.shape)
print(thres.shape)
# finding countours
contours, others = cv2.findContours(thres, mode = cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
blank = np.zeros(bilateral.shape, dtype='uint8')
cv2.drawContours(blank, contours=contours, contourIdx=-1, color=(0,255,0), thickness=1)
cv2.imshow('contours draw', blank)

cv2.waitKey(0)