from enum import Enum
import cv2
cap = cv2.VideoCapture(0)

class CaptureMode(Enum):
    SCREENSHOT = 0
    CAM = 1
  
def captureFrame(cap, mode):
    if(mode.value == 0):
        pass
    if(mode.value == 1):
        ret, img = cap.read()
        return img  
        
#def faceEquals(image1, image2):
