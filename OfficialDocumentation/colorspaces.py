import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]#.startswith checks the first value
print( flags )