import cv2 as cv
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    ret, frame = capture.read()
    if ret:
        cv.imshow('video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
        continue
    break

capture.release()
cv.destroyAllWindows()