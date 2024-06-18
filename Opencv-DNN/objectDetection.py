import os
import cv2 
import dlib
from time import time
import matplotlib.pyplot as plt

opencv_dnn_model = cv2.dnn.readNetFromCaffe(prototxt=r"C:\Users\mathe\OneDrive\Documentos\Opencv-DNN\deploy.prototxt",
                                            caffeModel=r"C:\Users\mathe\OneDrive\Documentos\Opencv-DNN\res10_300x300_ssd_iter_140000_fp16.caffemodel")


def cvDnnDetectFaces(image, opencv_dnn_model, min_confidence=0.5, display = True):

    image_height, image_width, _ = image.shape

    output_image = image.copy()

    preprocessed_image = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(300, 300),
                                               mean=(104.0, 117.0, 123.0), swapRB=False, crop=False)

    opencv_dnn_model.setInput(preprocessed_image)

    results = opencv_dnn_model.forward()    

    for face in results[0][0]:
        
        face_confidence = face[2]
        
        if face_confidence > min_confidence:

            bbox = face[3:]

            x1 = int(bbox[0] * image_width)
            y1 = int(bbox[1] * image_height)
            x2 = int(bbox[2] * image_width)
            y2 = int(bbox[3] * image_height)

            cv2.rectangle(output_image, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=2)

    if display:
        
        cv2.imshow('Detected Faces', output_image)
        cv2.waitKey(0)
        
    else:
        
        return output_image, results
    
image = cv2.imread('pessoas.jpg')

video = cv2.VideoCapture(r"C:\Users\mathe\OneDrive\Documentos\Opencv-DNN\video.mp4")

while True:
    video_return, video_frame = video.read()
    new_frame, results = cvDnnDetectFaces(video_frame, opencv_dnn_model, display=False)
    cv2.imshow('Detected Faces', new_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()