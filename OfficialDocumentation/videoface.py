from __future__ import print_function
import cv2 as cv
import argparse
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_alt.xml')



parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='data/haarcascades/haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
camera_device=args.camera
cap=cv.VideoCapture(camera_device)

while cap.isOpened():
    _,img=cap.read()


    
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,255,0),3)
    cv.imshow('img',img)

    if cv.waitKey(1) & 0xFF==ord('k'):
        break
cap.release()
cap.destroyAllwindows()