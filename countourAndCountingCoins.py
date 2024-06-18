import cv2 as cv
import numpy as np


img = cv.imread('Photos/coins.jpeg')
print(img.shape)
cv.imshow('Coins', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 30, 150)

(cnts,_) = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(len(cnts))
cv.drawContours(img,cnts, -1, (0,255,0), 2)
cv.imshow('Contours', img)
cv.waitKey(0)

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv.boundingRect(c)
    print("Coin #{}".format(i + 1))
    coin = img[y:y + h, x:x + w]
    cv.imshow('Coin', coin)

    mask = np.zeros(img.shape[:2], dtype='uint8')
    ((centerX, centerY), radius) = cv.minEnclosingCircle(c)
    cv.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    cv.imshow('Masked Coin', cv.bitwise_and(coin, coin, mask=mask))
    cv.waitKey(0)