
import cv2 as cv
import numpy as np
img=np.zeros((512,512,3),np.uint8)
img2=np.zeros((512,512,3),np.uint8)

 
mode=True
drawing=False
def do_nothing(r):  
    pass
def draw_circle(event,x,y,flags,param):
    global mode,drawing
    if mode==True:
        if event==cv.EVENT_LBUTTONDOWN:
            drawing=True
        elif event==cv.EVENT_MOUSEMOVE:
           
            if drawing==True:
                
                if mode==True:
                
                    cv.circle(img2,(x,y),3,(220,169,201),-1)
        elif event==cv.EVENT_LBUTTONUP:
        
            drawing=False


cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

cv.createTrackbar('R','image',0,255,do_nothing)# creates the Trackbar 
cv.createTrackbar('B','image',0,255,do_nothing)
cv.createTrackbar('G','image',0,255,do_nothing)


switch='0: OFF \n 1:ON'
cv.createTrackbar(switch,'image',0,1,do_nothing)
while(1):
    cv.imshow('image',img)
   

    k=cv.waitKey(1)&0XFF
    if k==ord('m'):
        mode=not mode

    if k==27:
        break #click escape to break  out the picture

    r=cv.getTrackbarPos('R','image')# gets the trackbar position that was created
    g=cv.getTrackbarPos('G','image')
    b=cv.getTrackbarPos('B','image')
    s=cv.getTrackbarPos(switch,'image')
    if s==0:
        img[:]=0
    else:
        img[:]=np.array([b,g,r]) # ! not the  most effective form !
        img = cv.add(img, img2)# add both images to img 



cv.destroyAllWindows()
