import cv2 as cv
import os
import uuid


PIC_PATH = os.path.join('People2', 'Matheus')
os.makedirs(PIC_PATH)


os.path.join(PIC_PATH, '{}.jpg'.format(uuid.uuid1()))

cap = cv.VideoCapture(0)

while cap.isOpened(): 
    ret, frame = cap.read() 

    if cv.waitKey(1) & 0XFF == ord('a'):
        imgname = os.path.join(PIC_PATH, '{}.jpg'.format(uuid.uuid1()))
        cv.imwrite(imgname, frame)
      
    cv.imshow('Image Collection', frame)
      
    if cv.waitKey(1) & 0XFF == ord('q'):
        break
        

cap.release()
cv.destroyAllWindows()