import cv2 as cv
import numpy as np

img = cv.imread('Photos/coins.jpeg')


# Laplaciano
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

# Sobel
sobelx = cv.Sobel(lap, cv.CV_64F, 1, 0)
sobely = cv.Sobel(lap, cv.CV_64F, 0, 1)
# combinedSobel = cv.bitwise_or(sobelx, sobely)
# stack = np.hstack((sobelx, sobely, combinedSobel))
# cv.imshow('Stack', stack)

sobelx2 = np.uint8(np.absolute(sobelx))
sobely2 = np.uint8(np.absolute(sobely))
sobelCombined2 = cv.bitwise_or(sobelx2, sobely2)
stack2 = np.hstack((sobelx2, sobely2, sobelCombined2))
cv.imshow('Stack2', stack2)
cv.waitKey(0)

#Canny
blur = cv.GaussianBlur(gray, (3,3), 0)
canny = cv.Canny(blur, 20, 100)
cv.imshow('Canny', canny)
cv.waitKey(0)

#Auto canny
v = np.median(img)
lower = int(max(0, (1.0 - 0.33) * v))
upper = int(min(255, (1.0 + 0.33) * v))
autoCanny = cv.Canny(blur, lower, upper)
cv.imshow('Auto Canny', autoCanny)
cv.waitKey(0)


