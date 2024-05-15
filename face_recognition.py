import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')


#features = np.load('features.npy')
#labels = np.load('labels.npy')

people = ['Justin Bieber', 'The Weeknd']
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')


img = cv.imread('Photos/jennie.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)


# Detect the face in the image

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 5)
for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(face_roi)
    print(f' {people[label]} % de certeza {confidence}')
    if confidence > 50:
        cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    else:
        cv.putText(img, 'WHO', (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2)
        cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255), thickness=2)


cv.imshow('Detected face', img)

cv.waitKey(0)





