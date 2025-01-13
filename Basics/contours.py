# Here we have tried to find the contours using two methods
#1. by using the Canny edge detection method, which is ideally perfect option to go initially.
#2. By using the thresholding the binary image. Should not be used directly, first try with 1 option.

import cv2
import numpy as np

img = cv2.imread('./images/cats.jpg')
cv2.imshow('cats', img)

blank = np.zeros(shape= img.shape, dtype='uint8')
cv2.imshow('blank', blank)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray img', gray)

blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('blur', blur)

# canny = cv2.Canny(blur, 125, 175)
# cv2.imshow('canny edges', canny) 

# It just remove the pixel whose value are below 125
ret, thres = cv2.threshold(blur, thresh= 125, maxval=255, type= cv2.THRESH_BINARY)
cv2.imshow('threshold', thres)

contours, hirarchies = cv2.findContours(thres, mode= cv2.RETR_LIST, method= cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

# print(cv2.CHAIN_APPROX_NONE)  # this consider each of the points in the line as a seperate contour
# print(cv2.CHAIN_APPROX_SIMPLE) # this consider only the start and end point of the line as contour, which is ideally correct.

cv2.drawContours(image= blank, contours= contours, contourIdx= -1, color= (0,255,0), thickness=2)
cv2.imshow('contours drawn', blank)


cv2.waitKey(0)


