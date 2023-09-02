# Reading Images:>>


# import cv2 as cv

# img=cv.imread('Resources/no1image.jpeg')

# cv.imshow('image1',img)
# cv.waitKey(0)

# Reading Videos :>>

# import cv2 as cv
# cap=cv.VideoCapture('Resources/video1.mp4')
# while True:
#     sucess, img=cap.read()
#     cv.imshow('Video',img)
#     if cv.waitKey(1) & 0xFF ==ord('q'): # pressing q break out of the loop
        # break
# Using a Webcam
 #cap=cv.Video(1)

 #Using my camera for Video:
import cv2 as cv
cap=cv.VideoCapture(0)
cap.set(3,640) #3 > width
cap.set(4,480) #4 is the height
cap.set(10,100) #10 is the brightness
while True:
    sucess, img=cap.read()
    cv.imshow('Video',img)
    if cv.waitKey(1) & 0xFF ==ord('y'): 
        break

cv.waitKey(0)