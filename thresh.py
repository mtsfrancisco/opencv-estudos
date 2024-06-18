import cv2 as cv
import mahotas


img = cv.imread('Photos/Cat.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 4)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# Opencv Otsu
T, otsu = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow('Opencv Otsu', otsu)

# Mahotas otsu
T = mahotas.thresholding.otsu(gray)
print(f'Mahotas Otsu threshold: {T}')
thresh = gray.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh= cv.bitwise_not(thresh) # Invert the colors = cv2.THRESH_BINARY_INV
cv.imshow('Mahotas Otsu', thresh)

# Mahotas Riddler-Calvard
T = mahotas.thresholding.rc(gray)
print(f'Mahotas Riddler-Calvard threshold: {T}')
thresh = gray.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh= cv.bitwise_not(thresh)  # Invert the colors = cv2.THRESH_BINARY_INV
cv.imshow('Mahotas Riddler-Calvard', thresh)


cv.waitKey(0)