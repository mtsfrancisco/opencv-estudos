import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Photos/minion.png')
cv2.imshow('Minion', img)
cv2.waitKey(0)