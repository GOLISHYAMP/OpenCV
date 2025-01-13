import cv2 as cv
import numpy as np

blank = np.zeros((255, 255, 3), dtype='uint8')
cv.rectangle(blank, pt1=(50,50), pt2=(150,150), color=(255, 0, 0), thickness=-1)
cv.circle(blank, center=(50,50), radius= 40, color=(0,255,0), thickness=-1)
cv.line(blank, (10,10), (150, 150), color=(255, 255, 255), thickness= 3)
cv.putText(blank, text="Hii, I am learning opencv", org=(0,20), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=0.5, color=(0, 0, 255), thickness=2)
cv.imshow('blank', blank)
cv.waitKey(0)