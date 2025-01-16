import cv2
import os
import numpy as np

features = []
labels = []

DIR = 'Resources/Faces/train'
path_faceDetector = 'Resources/haarcascade_frontalface_default.xml'

def trainer():
    haar_cascade = cv2.CascadeClassifier(path_faceDetector)
    People = os.listdir(DIR)

    for people in People:
        people_dir = os.path.join(DIR, people)
        label = People.index(people)
        for img_path in os.listdir(people_dir):
            img = cv2.imread(os.path.join(people_dir, img_path))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (15, 15), 10)
            rect_coods = haar_cascade.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=1)
            for (x, y, w, h) in rect_coods:
                faces_roi = gray[y:y+h , x:x+w]
                features.append(faces_roi)
                labels.append(label)

trainer()
print(f"{len(features)}, {len(labels)}")
features = np.array(features, dtype='object')
labels = np.array(labels)
np.save('features.npy', features)
np.save('labels.npy', labels)

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer =  cv2.face.LBPHFaceRecognizer_create()

# Train the face recognizer
face_recognizer.train(features, labels)
face_recognizer.save('face_recognizer.yml')

