# Rescaling means modifying the height and width
# To a pacticualar height and width
# CTRL+/ comments the entire line of code

import cv2 as cv

img=cv.imread('Photos/cat.jpg')



def changeRes(width,height): 
  # This methods only works for live videos
  capture.set(3,width)
  capture.set(4,height)

def rescaleFrame(frame,scale=0.75): #created a function for not live videos 
  width=int(frame.shape[1]*scale) # shape[1] >> width of the image
  height=int(frame.shape[0]*scale) # shape [0] >> height of the image
  dimension=(width,height)

  return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('Videos/dog.mp4') 
resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)

while True:

  isTrue,frame=capture.read() 
  frame_resized=rescaleFrame(frame)
  
  cv.imshow('DogMoving',frame) 
  cv.imshow('Video Resized',frame_resized)

  if cv.waitKey(20) & 0xFF==ord('y'):



    break
print(frame)
capture.release() 

cv.destroyAllWimdows()
Windows() 
cv.waitKey(0)