import cv2
import numpy as np

img = cv2.imread('../Resources/images/cats.jpg')
cv2.imshow('img', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

B,G,R = cv2.split(img)
cv2.imshow('redimg', R)
cv2.imshow('blueimg', B)
cv2.imshow('greenimg', G)

merged = cv2.merge([B,G,R])
cv2.imshow('Merged',merged)

redMerge = cv2.merge([blank,blank, R])
cv2.imshow('redMerge', redMerge)
blueMerge= cv2.merge([B,blank,blank])
cv2.imshow('blueMerge', blueMerge)
greenMerge = cv2.merge([blank, G, blank])
cv2.imshow('greenMerge', greenMerge)

cv2.waitKey(0)