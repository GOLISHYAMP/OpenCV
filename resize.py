import cv2 as cv

def rescale_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

# img = cv.imread('images/cat_large.jpg')
# rescaled_img = rescale_frame(img, 0.3)
# cv.imshow('cat', rescaled_img)
# cv.waitKey(0)

import cv2 as cv
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    ret, frame = capture.read()
    if ret:
        resized_frame = rescale_frame(frame, scale=0.5)
        cv.imshow('video', resized_frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
        continue
    break

capture.release()
cv.destroyAllWindows()