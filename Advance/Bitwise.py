

import cv2
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), color= 255, thickness=-1)
cv2.imshow('Rectangle', rectangle)

circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)
cv2.imshow('Circle', circle)

# Bitwise AND
bitwiseAND = cv2.bitwise_and(rectangle, circle)
cv2.imshow('BitwiseAND', bitwiseAND)

# Bitwise OR
bitwiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow('BitwiseOR', bitwiseOR)

# Bitwise XOR
bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('BitwiseXOR', bitwiseXOR)

cv2.waitKey(0)