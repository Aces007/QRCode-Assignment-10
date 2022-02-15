from base64 import decode
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime

# QRKo = cv2.imread('frame.png')
CamTime = cv2.VideoCapture(0)
CamTime.set(3,640)
CamTime.set(4,480)


while True:
    success, QRKo = CamTime.read()
    

    for codes in decode(QRKo):
        print(codes.data)
        MyTxt = open('Personal.txt', 'w')
        DecodeData = codes.data.decode('utf-8')
        print(DecodeData)


        Dimensions = np.array([codes.polygon], np.int32)
        Dimensions = Dimensions.reshape(-1,1,2)
        cv2.polylines(QRKo,[Dimensions], True, (255,0,255), 5)


        # Record Date
        RealTime = datetime.now()
        MyTxt.write(RealTime.strftime("Present Date: %B/%d/%Y \n"))
        MyTxt.write(RealTime.strftime("Current Time: %H:%M:%S"))
        MyTxt.close()

    cv2.imshow('Result', QRKo)
    cv2.waitKey(1)

