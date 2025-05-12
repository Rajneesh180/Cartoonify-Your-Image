#17. CLICK BUTTON PROJECT

import cv2
import numpy as np

#create a black image and window
windowName = 'Drawing'
cv2.namedWindow(windowName)
img = np.zeros((500,500,3))

#mouse call back function
#flags and param are not used at all , but we need to write it in any mousecallback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: #left button double click
        cv2.circle(img,(x,y),40,(0,255,0),-1) #src, coordinates , radius

    if event == cv2.EVENT_RBUTTONDBLCLK: #right button double click
            cv2.circle(img,(x,y),30,(255,255,255),-1)

    if event == cv2.EVENT_LBUTTONDOWN: #left  click
        cv2.circle(img,(x,y),20,(0,255,255),-1)

    if event == cv2.EVENT_RBUTTONDOWN: #right click
        cv2.circle(img,(x,y),20,(0,0,255),-1)

cv2.setMouseCallback(windowName,draw_circle) #function call
while(True):
    cv2.imshow(windowName , img)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
