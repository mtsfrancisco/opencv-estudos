import cv2 as cv

#Abrir imagem e mostrar
"""
img = cv.imread('Photos\Cat.jpg') #
cv.imshow('Cat', img) #mostra a imagem em uma tela

cv.waitKey(0)
"""

#Lendo videos
capture = cv.VideoCapture("Videos\miau.mp4") # 0 como argumento abre a webcam

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows

