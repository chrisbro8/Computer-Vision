import cv2 as cv

import numpy as np # This is importing the numpy as {np}

#Two ways of drawing 
#  1:>>This creates a blank image to draw on
blank=np.zeros((500,500,3),dtype='uint8') #500 by 500 is the shape size
# (<height of the image>,<width of the image>,<number of colour channels=3>)
#dtype:>data type
cv.imshow('Blank',blank) # :> This just bring a blank empty box
 

 # 1. Point the image a certains colour:
# blank[:]=0,255,0 # --(RGB),This is  all entire array to a certain color
# blank[0:100,0:500]=(255,0,0)  # coloring a certain portion of the blank // or all
# blank[<height range>,<width range>]=<color in RGB>
# cv.imshow('Colouring_Green',blank)





# 2 ...Drawing a Rectangle
# cv.Rectangle(image,point1,point2,color(RGB),thickness=(in inttegers))
# cv.rectangle(blank,(0,400),(500,10),(0,255,0),thickness=-1)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1) # This skwed the height and width of the images half time the normal size


# filling in image inside ,thickness=cv.FILLED
# or thickness=-1

# 3:> Drawing a Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.circle(imgread,<center>,<radius>,<color>,<thickness in integer>))


# 4:>Drawing a Line
cv.line(blank,(100,250),(blank.shape[1]//2,500),(255,255,255),thickness=3) # exactly like the rectangle


# 5. Write a Text in an image
cv.putText(blank,'Hello my name is brownwell',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255),thickness=2) #<cv.FONT_HERSHEY_TRIPLEX> this is a type of font
# cv.putText(image, text, position, cv.FONT_HERSHEY_TRIPLEX, font_scale, color, thickness),1.0 is the font scale

cv.imshow('Drawing',blank)

cv.waitKey(0)
