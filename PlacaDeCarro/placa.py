
import cv2 as cv
import numpy as np
from skimage.segmentation import clear_border


haar_cascade = cv.CascadeClassifier('/Users/mtsfrancisco/Documents/Opencv-freecodecamp/PlacaDeCarro/haarcascade_russian_plate_number.xml')


cap = cv.VideoCapture('/Users/mtsfrancisco/Documents/Opencv-freecodecamp/PlacaDeCarro/PlateVideo.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    plate_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x,y,w,h) in plate_rect:    
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Video', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

