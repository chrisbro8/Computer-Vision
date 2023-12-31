import cv2 as cv

face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the image input
img=cv.imread('Resources/roi.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,3)
print(faces)

for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
cv.imshow('img',img)
cv.waitKey(0)