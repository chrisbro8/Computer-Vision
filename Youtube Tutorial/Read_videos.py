import cv2 as cv #name alias to cv

capture=cv.VideoCapture('Videos/dog.mp4') 


# :VideoCapture(<int>): This conect directly to my camera and webcam 

# Where (integers:0,1,2,3,4 and e,t,c) represent if conects cameras or webcam

#Using<adress/videoname> plays a stored 
outside_sucess=True

while outside_sucess: ## read the videos frame by frame

  sucess,frame=capture.read() ##capture.read():reads the video frame by frame
  outside_sucess=sucess
  if not outside_sucess:#To trap the error after all the codde has ran
    print (outside_sucess)
    break

  
  cv.imshow('DogMoving',frame) #Displaying individual frame ina loop
  #DogMoving is the Video  name when it runs ir can be anyname

  if cv.waitKey(22) & 0xFF==ord('y'):
  # 0xFF==ord(<anyletter>) :>If the letter is pressed the video is closed before it finishes
  # cv.waitKey(<Speed at which the images is played in,the higher the number the lower the speed>)

    break

## Exited the loop


capture.release()  #release the capture

cv.destroyAllWindows() #Destroy all
#  cv.waitKey(0)


'''
The Error after the video show it ran put of frames to diplay then
broke out of the loop
 '''
