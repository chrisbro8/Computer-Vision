import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,5222,3), np.uint8)
x=cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.imshow('Drawn_Circle',x)
imgcrop=img[0:200,380:600]
cv.imshow('img',imgcrop)
print(img)
print(imgcrop)
cv.waitKey(0)