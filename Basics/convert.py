import cv2 as cv
img = cv.imread('images/my_photo.jpg')
cv.imshow('cat', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', RGB)

cv.waitKey(0)