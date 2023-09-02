import cv2 as cv
import numpy as np

img=cv.imread('Resources/no2image.png')
print(img.shape) #This prints the size of the image and
#Lists of color channel which is 3: E.g BGR

imgresize=cv.resize(img,(300,200)) #original image size
# cv.imshow('Image',img) <<This is the original image,300 is width ans 200 is height
cv.imshow('Image',imgresize)
print(imgresize.shape) #resize image size

# Cropping Images:slicing the array
# Height comes first before width
imgcrop=img[0:200,200:500]
print(imgcrop)
cv.imshow('ImageCropped',imgcrop)









cv.waitKey(0)
