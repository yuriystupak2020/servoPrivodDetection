import cv2
import sys
import time
import numpy as np
# from servoptivod_file1 import *

# cascPath = 'haarcascade_frontalface_default.xml'
# faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

x_T = 300
y_T = 220


# Load the pre-trained model for face detection
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000_fp16.caffemodel")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

while True:
    ret, frame = video_capture.read()

    frame = cv2.resize(frame, (640, 480))
    cv2.putText(frame, "T", (x_T, y_T), cv2.FONT_HERSHEY_SIMPLEX, 1, (55, 50, 250), 4)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], False, False)

    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([640, 480, 640, 480])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            print((x_T - (startX + endX) / 2 - startX / 2 + 120), (y_T - (startY + endY) / 2 - startY / 2 + 40))
            # pig_pio_detection()

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
