import numpy as np
import cv2
from mss import mss
from modules import *

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

mode = CaptureMode.CAM

padTop = 160
padLeft = 160
width = 640
height = 480

cap.set(3,640) # set Width
cap.set(4,480) # set Height
mon = {'top': padTop, 'left': padLeft, 'width': width, 'height': height}

face_id = input('\n enter user id end press  ==>  ')

counter = 0

while True:
    image = captureFrame(cap, mode)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = image[y:y+h, x:x+w]
        
        cv2.imwrite("Faces/User." + face_id + '.' + str(counter) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', image)
        counter += 1

    cv2.imshow('video',image)

    k = cv2.waitKey(100) & 0xff
    if k == 27: 
        break
    if counter > 300:
        break

cap.release()
cv2.destroyAllWindows()


