import numpy as np
import cv2 as cv
# mouse callback function
def draw_any(event,x,y,flags,param):
   if event == cv.EVENT_LBUTTONDBLCLK:
      cv.circle(img,(x,y),5,(255,0,255),-1)


# Create a black image, a window and bind the function to window

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_any)
while(1): #1 is True
 cv.imshow('image',img)
 if cv.waitKey(20) & 0xFF ==ord( 'y'):
    break
