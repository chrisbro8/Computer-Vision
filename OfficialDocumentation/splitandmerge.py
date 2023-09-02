import cv2 as cv
import numpy as np
imgx=cv.imread('Resources/roi.jpg')
b,g,r=cv.split(imgx)
x=(b,g,r)



# Arihemetic Operations on Images
img=cv.imread('Resources/no3image.jpeg')
cx=np.uint8([250])

cv.waitKey(0)