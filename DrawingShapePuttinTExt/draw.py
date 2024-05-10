import cv2 as cv
import numpy as np


blank = np.zeros((500,500, 3), dtype='uint8')

# 1. Pintar a imagem de alguma cor
blank[200:300, 300:400] = 0,0,255
cv.imshow("Green", blank)

#2. Desenha um retangulo
cv.rectangle(blank, (100,400), (250,250), (0,255,0), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)

#3. Desenha um circulo
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
cv.imshow("Circle", blank)

#4. Desenhar uma linha
cv.line(blank, (100,400), (250,250), (255,255,255), thickness=3)
cv.imshow("Line", blank)

#5. Texto
cv.putText(blank, 'Matheus esquece', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Hello', blank)

cv.waitKey(0)

