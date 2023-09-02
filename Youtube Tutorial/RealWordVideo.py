import cv2 as cv
cap=cv.VideoCapture(0)
while True:
  sucess,img=cap.read()
  cv.imshow("Img",img)

  if  cv.waitKey(22)& 0xFF==ord('y'):
    break

  cv.waitKey(1)