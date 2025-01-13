import numpy as np
import cv2

img = cv2.imread('../Resources/images/cats.jpg')
cv2.imshow('Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# mask = cv2.circle(blank, ( (img.shape[1]//2) -10, img.shape[0]//2), radius=200, color=255, thickness=-1 )
mask = cv2.rectangle(blank, (100, 100), (500, 300), color=255, thickness=-1)
cv2.imshow('mask', mask)

bitwiseAND = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('MASKED', bitwiseAND)

cv2.waitKey(0)