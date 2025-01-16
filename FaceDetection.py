import cv2

# img = cv2.imread('Resources/images/multiple_faces2.jpg')
# cv2.imshow('Image', img)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if ret:
        #Gray image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", gray)

        blur = cv2.GaussianBlur(gray, (15, 15), 9)
        cv2.imshow("BLUR", blur)

        haar_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
        faceRectangles = haar_cascade.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=8)
        print(f"No of faces identified in the image is : {len(faceRectangles)}")
        # print(faceRectangles)
        for x, y, w, h in faceRectangles:
            cv2.rectangle(img, (x, y), (x+w, y+h), color= (0, 255, 0), thickness=2)
        cv2.imshow('Detected faces', img)
        if cv2.waitKey(20) & 0xFF==ord('d'):
            break
        continue
    break

cap.release()
cv2.destroyAllWindows()
# cv2.waitKey(0)