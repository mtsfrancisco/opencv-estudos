import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')



#features = np.load('features.npy')
#labels = np.load('labels.npy')



people = ['Matheus', 'Malta']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')



# Detect the face in the image
def detect_face(img, haar_cascade, face_recognizer, people):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, minNeighbors=6)

    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(faces_roi)
        if confidence > 15:
            print(f'Label = {people[label]} with a confidence of {confidence}')
            cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
            cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
        else :
            print('people{label}', confidence)
            cv.putText(img, 'Unknown', (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,0,0), thickness=2)
            cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    cv.imshow('Detected face', img)


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    detect_face(frame, haar_cascade, face_recognizer, people)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break


cv.waitKey(0)





