import numpy as np
from datetime import datetime
import cv2
from pyzbar.pyzbar import decode

ItoQRKo = cv2.imread('ItoQRCodeKo.png')

for codes in decode(ItoQRKo):
    print(codes.data)
    TheDataInside = codes.data.decode('utf-8')
    print (TheDataInside)