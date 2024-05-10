import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale) # frame.shape[1] width do frame
    height = int(frame.shape[0] * scale) # frame.shape[0] height do frame
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('Photos\Cat.jpg') 
cv.imshow('Cat', img)

resized_img = rescaleFrame(img)
cv.imshow('Resized Cat', resized_img)



capture = cv.VideoCapture("Videos\miau.mp4") # 0 como argumento abre a webcam

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows




cv.waitKey(0)