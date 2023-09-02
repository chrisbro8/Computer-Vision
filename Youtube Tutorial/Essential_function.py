import cv2 as cv

img=cv.imread('Photos/Cat.jpg')
cv.imshow('Picture1',img)
# i have to use seperate names else the image re-refers


# Converting to GrayScale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray#Picture',gray)













cv.waitKey(0)