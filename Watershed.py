import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def watershed():
    img = cv2.imread("Photos/pikachu2ComBackground.webp")
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.figure()
    plt.subplot(231)
    plt.imshow(img, cmap='gray')
    
    plt.subplot(232)
    imgThresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY+cv2.THRESH_BINARY_INV,13,7)
    plt.imshow(imgThresh, cmap='gray')

    plt.subplot(233)
    kernel = np.ones((3,3), np.uint8)
    imgDilate = cv2.dilate(imgThresh, kernel)
    #imgDilate = cv2.morphologyEx(imgThresh, cv2.MORPH_DILATE, kernel)
    plt.imshow(imgDilate, cmap='gray')
    distTrans = cv2.distanceTransform(imgThresh, cv2.DIST_L2, 5)

    plt.show()


watershed()