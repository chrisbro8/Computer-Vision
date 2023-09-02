import cv2 as cv
import numpy as np
img=cv.imread('Resources/roi.jpg')
print(img.shape)
ball=img[230:277,260:318] # first one is height and the second is width
assert img is not None ,"Picture Errror"
cv.imshow('Img',ball)

cv.waitKey(0)


