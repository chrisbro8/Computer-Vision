#extract blue green and red images simultaneuosly
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
while(1):
    _,frame=cap.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_red= np.array([0,50,50])
    lower_blue=np.array([100,50,50])
    lower_green=np.array([35,50,50])
    upper_blue=np.array([140,255,255])
    upper_red=np.array([20,255,255])
    upper_green=np.array([85,255,255])

    maskblue=cv.inRange(hsv,lower_blue,upper_blue)
    maskgreen=cv.inRange(hsv,lower_green,upper_green)
    maskred=cv.inRange(hsv,lower_red,upper_red)
    res1=cv.bitwise_and(frame,frame,mask=maskblue)# operations on the frame and masked images
    res2=cv.bitwise_and(frame,frame,mask=maskgreen)
    res3=cv.bitwise_and(frame,frame,mask=maskred)

    cv.imshow('frame',frame)
    cv.imshow('res1',res1)
    cv.imshow('res2',res2)
    cv.imshow('res3',res3)
    k=cv.waitKey(10) & 0xFF
    if k==27:
        break

cv.destroyAllWindows()

