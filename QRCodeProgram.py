import numpy as np
from datetime import datetime
import cv2
from pyzbar.pyzbar import decode

# Necessary for calling the webcam installed on your computer
CameraTime = cv2.VideoCapture(0)
CameraTime.set(3,640)
CameraTime.set(4,480)

while True:
    success, ItoQRKo = CameraTime.read()
    for codes in decode(ItoQRKo):
        
        # Responsible for printing the data I inserted in the QR Code
        print(codes.data)
        MyTxt = open('Personal.txt', 'w')
        TheDataInside = codes.data.decode('utf-8')
        print(TheDataInside)

        
        # BorderLine Authentication
        Dimensions = np.array([codes.polygon], np.int32)
        Dimensions = Dimensions.reshape(-1,1,2)
        cv2.polylines(ItoQRKo,[Dimensions], True, (255,0,255), 5)
        
        
        # Record Date
        RealTime = datetime.now()
        RealDateOpen = RealTime.strftime("Present Date: %B/%d/%Y \n")
        RealTimeThen = RealTime.strftime("Latest Time: %H:%M:%S")


        # Responsible for rewriting the contents of the code to the txt file I assigned above
        MyTxt.write(f'{TheDataInside}\n{RealDateOpen}{RealTimeThen}')
    
        
    cv2.imshow('Result', ItoQRKo)
    cv2.waitKey(1)

