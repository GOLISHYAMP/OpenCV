import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Resources/images/cats.jpg')
cv2.imshow('Image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)

gray_hist = cv2.calcHist([img], channels=[0], mask= None, histSize=[256], ranges=[0, 256])
plt.figure()
plt.title('Gray Hist')
plt.xlabel("Bins")
plt.ylabel('pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)