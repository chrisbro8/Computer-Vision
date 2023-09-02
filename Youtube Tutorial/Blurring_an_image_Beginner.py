import cv2 as cv

img=cv.imread('Photos/Cat.jpg')
cv.imshow('OriginalImage',img)
# Blurring an image
#The blur could be any name# 
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)#<(src),(ksize),(bordertype)>
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)#<(src),(ksize),(bordertype)>
# ksize should be in odd number
cv.imshow('Blurred_Image',blur)













cv.waitKey(0)