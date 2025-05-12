# 19. MY CANNY SKETCH (EDGE DETECTION)

import cv2

cap = cv2.VideoCapture(0) #0 reserves the default web cam port

while True:
    ret,frame = cap.read()
    canny = cv2.Canny(frame,20,150) #20,150 are thresh values for best canny pictures or video
    cv2.imshow('My Canny Sketch',canny)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()

    
