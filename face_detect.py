import cv2 as cv
import numpy as np

img = cv.imread('Photos/weeknd.jpeg')
cv.imshow('Pessoa', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

capture = cv.VideoCapture(0) # 0 como argumento abre a webcam


while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x,y,w,h) in faces_rect:    
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Faces', frame)    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

