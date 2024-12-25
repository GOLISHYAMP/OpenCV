import cv2 as cv
img = cv.imread('images/cat_large.jpg')
cv.imshow('cat', img)
cv.waitKey(0)