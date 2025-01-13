#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread('images/my_photo.jpg')
cv.imshow('photo', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Cropping
cropped = blur[30:550, 430:850]
cv.imshow('Cropped', cropped)

# Edge Cascade
canny = cv.Canny(cropped, threshold1=50, threshold2= 90)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# # Eroding
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


cv.waitKey(0)
