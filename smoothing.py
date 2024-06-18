import cv2 as cv
import numpy as np

img = cv.imread('Photos/Cat.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
#bilateral = cv.bilateralFilter(img, 10, 35, 25)
bilateral = np.hstack([cv.bilateralFilter(img, 5, 21, 21),
                       cv.bilateralFilter(img, 7, 31, 31),
                       cv.bilateralFilter(img, 9, 41, 41)])
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)