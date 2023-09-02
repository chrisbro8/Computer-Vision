import numpy as np
import cv2 as cv

im=cv.imread('Resources/roi.jpg')

imgray=cv.cvtColor(im,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(imgray,127,255,0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
im2 = cv.drawContours(imgray.copy(), contours, -1, (0, 255, 0), 2)

# Display the result or do further processing
cv.imshow('Original',im)
cv.imshow('Contours', im2)
cv.waitKey(0)
cv.destroyAllWindows()