#7.SOLID COLORS - RED,BLUE,GREEN
#RED color background

import numpy as np
import cv2
img = np.zeros((250,250,3))#black background
#img[:] will select the whole image
img[:] = 0,255,0 #we assign the color(B,G,R)

cv2.imshow('GREEN',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
