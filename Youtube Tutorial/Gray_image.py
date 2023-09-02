import cv2 as cv    # : This is importing the open cv library and giving the cv2 an alias name of CV

img=cv.imread('Photos\Cat.jpg')  #: imread-read a pacticular image and Photos is the directory the cat image is stored,
                                 #   :Any name can be used inplace of img...abs

cv.imshow('BigCat',img) #: Dispalys the image as a new window (<'ImageName'>,<The read objectname>)

cv.waitKey(0) #:Wait for sometime for a keyboard key to be pressed key(<Timer on how long the image would stay>)
                  #:If <0> is put the image wont exist the screeen until a key(alphabet or numbers)is pressed 


## Note Images Larger than screen size would not be dispalyed

##To run use the termial< python (filename)>