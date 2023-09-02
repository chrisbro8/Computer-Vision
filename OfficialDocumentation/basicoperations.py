import numpy as np
import  cv2 as cv

# 1...
# img=cv.imread('exist.jpg')
# assert img is not None,"File could not be read check path"


#2
img=cv.imread("Resources/no3image.jpeg") #it a forward slash not a backward slash
px=img
print(px)
blue=img[100,100,0]
print(blue)
#modify pixel
img[100,100]=[255,255,255]
print(img[100,100])