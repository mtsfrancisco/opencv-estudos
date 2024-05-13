import cv2 as cv
import numpy as np

img = cv.imread('Photos/Cat.jpg')
cv.imshow('Cat', img)


# Laplaciano
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)

combinedSobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combinedSobel)



cv.waitKey(0)