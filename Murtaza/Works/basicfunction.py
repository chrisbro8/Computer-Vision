import cv2 as cv
import numpy as np
img=cv.imread('Resources/no3image.jpeg')

#Convert to GrayScale
imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',imgGray)


#Blur an Image
imgBlur=cv.GaussianBlur(img,(7,7),0) #7 s and 7 has to be odd numbers
cv.imshow('Blurred_Image',imgBlur)


#Edge Detector
# 1 Canny
imgcanny=cv.Canny(img,100,100)
cv.imshow('Canny Image',imgcanny)

# Dialation for catching space in a canny image
kernel=np.ones((5,5),np.uint8)
imgDiliate=cv.dilate(imgcanny,kernel,iterations=1)
cv.imshow('Dialated_Image',imgDiliate)

# Erosion is the opposite of dialation make it thinneer
imgErode=cv.erode(imgDiliate,kernel,iterations=1)
cv.imshow('Eroded Image',imgErode)




cv.waitKey(0)