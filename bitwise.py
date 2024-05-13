import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")


rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)


# Bitwise AND (Intersecao)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwiseand", bitwise_and)

# Bitwise OR (Soma das imagnes)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwiseor", bitwise_or)

# Bitwise XOR (Apenas onde as imagens nao intersectam)
bitwise_xor = cv.bitwise_xor (rectangle, circle)
cv.imshow("Bitwisexor", bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitwise_not)

cv.waitKey(0)