# Here in this colorspace we learned about the different types of the colorspace.
# like RGB, BGR, GRAY, HSV, LAB
# In OPENCV the image is read and display as BGR, where as in the out of the opencv,
#  the image is processed as the RGB



import cv2
import matplotlib.pyplot as plt
BGR = cv2.imread('../Resources/images/my_photo.jpg')
cv2.imshow('BGR', BGR)

gray = cv2.cvtColor(BGR, cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY', gray)

gray2HSV = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.imshow("GRAY2HSV", gray2HSV)

HSV = cv2.cvtColor(BGR, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', HSV)

# HSV->BGR
HSV2BGR = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV2BGR', HSV2BGR)

LAB = cv2.cvtColor(BGR, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", LAB)

RGB = cv2.cvtColor(BGR, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", RGB)

plt.imshow(RGB)
plt.show()

plt.imshow(BGR)
plt.show()



cv2.waitKey(0)