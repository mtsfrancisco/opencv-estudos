import cv2 as cv

capture = cv.VideoCapture(0)
isTrue, frame = capture.read()

cv.imshow("Teste Camera", frame)

cv.waitKey(0)