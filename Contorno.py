import cv2 as cv


video = cv.VideoCapture('Videos/bombay traffic.mp4')


def grayScaleAndCountorn(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)

    canny = cv.Canny(blur, 125, 175) 
    #laplacian = cv.Laplacian(gray, cv.CV_64F)
    
    #sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
    #sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
    #combined_sobel = cv.bitwise_or(sobelx, sobely)


    return canny


while True:
    isTrue, frame = video.read()

    frameTratado = grayScaleAndCountorn(frame)
    cv.imshow('Trafego', frameTratado)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


video.release()
cv.waitKey(0)