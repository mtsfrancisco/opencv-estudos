import cv2 as cv

img = cv.imread('Photos/Cat.jpg')
cv.imshow('Cat', img)

#1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#2. Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#3. Edge Cascade ( Edges da imagem)
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

#4. Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

#5. Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("Eroded", eroded)

#6. Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) #o valor em interpolation depende do tamanho do resize
cv.imshow("Resized", resized)

#7, Crop
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)