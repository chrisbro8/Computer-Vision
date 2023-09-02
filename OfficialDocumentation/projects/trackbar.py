import cv2 as cv
import numpy as np
 

def do_nothing(r):  
    pass

img=np.zeros((512,512,3),np.uint8)
cv.namedWindow('image')

cv.createTrackbar('R','image',0,255,do_nothing)# creates the Trackbar 
cv.createTrackbar('B','image',0,255,do_nothing)
cv.createTrackbar('G','image',0,255,do_nothing)


switch='0: OFF \n 1:ON'
cv.createTrackbar(switch,'image',0,1,do_nothing)
while(1):
    cv.imshow('image',img)

    k=cv.waitKey(1)&0XFF

    if k==27:
        break #click escape to break  out the picture

    r=cv.getTrackbarPos('R','image')# gets the trackbar position that was created
    g=cv.getTrackbarPos('G','image')
    b=cv.getTrackbarPos('B','image')
    s=cv.getTrackbarPos(switch,'image')
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]



cv.destroyAllWindows
