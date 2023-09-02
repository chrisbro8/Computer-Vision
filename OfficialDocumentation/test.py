import cv2 as cv
import numpy as np

mode = True
drawing = False

def do_nothing(r):
    pass

def draw_circle(event, x, y, flags, param):
    global mode, drawing, img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.circle(img, (x, y), 5, (0, 255, 0), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

cv.createTrackbar('R', 'image', 0, 255, do_nothing)
cv.createTrackbar('B', 'image', 0, 255, do_nothing)
cv.createTrackbar('G', 'image', 0, 255, do_nothing)

switch = '0: OFF \n1: ON'
cv.createTrackbar(switch, 'image', 0, 1, do_nothing)

while True:
    cv.imshow('image', img)

    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode

    if k == 27:
        break

    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()
