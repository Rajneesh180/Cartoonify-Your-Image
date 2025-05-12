#18.ACCESSING THE WEBCAM USING PYTHON AND OPENCV

import cv2

cap = cv2.VideoCapture(0)#0 takes the default camera of out laptop

while True:
    ret,frame = cap.read() # It is reading the video from my port
    #ret and frame are 2 variable to be taken,but onlt frame will
    #be used and ret is dummy variable
    cv2.imshow('My Live Sketch',frame)
    if cv2.waitKey(1) == 13:
        break

cap.release() # It releases the port number
#make sure we perform cap.release,if not the webcam drivers may
#get corrupted
cv2.destroyAllWindows()
