import cv2 as cv
import numpy as np
img=np.zeros((512,512,3),np.uint8)
x=cv.rectangle(img,(0,0),(512,512),(0,255,0),3)
cv.imshow('rectangle',x)
cv.waitKey(0)