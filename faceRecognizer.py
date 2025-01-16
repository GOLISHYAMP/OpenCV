import cv2
import os
import numpy as np

haar_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recognizer.yml')

Peoples = os.listdir('Resources/Faces/train')

test_img = cv2.imread('Resources/Faces/val/mindy_kaling/3.jpg')
cv2.imshow('Image', test_img)

gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
blur = cv2.GaussianBlur(gray, (15, 15), 10)
cv2.imshow("Blue", blur)
rect_coords = haar_cascade.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=1)

for (x, y, w, h) in rect_coords:
    face_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(face_roi)
    cv2.rectangle(test_img, (x, y), (x+w, y+h), color=(0, 255, 0), thickness=2)
    cv2.putText(test_img, text=Peoples[label], org = (x-10,y-10), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0, 255, 0), thickness= 1)

cv2.imshow('Detected person', test_img)

cv2.waitKey(0)
