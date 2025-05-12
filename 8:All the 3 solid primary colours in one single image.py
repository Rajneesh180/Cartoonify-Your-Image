#8.All the 3 solid/primary colors in one single image

import cv2
import numpy as np
img = np.zeros((300,300,3))#creates a black background
#img[y -coordinate,x-coordiante]
img[0:100,0:300] = 0,255,0 # GREEN COLOR
img[100:200,0:300] = 0,0,255 #RED COLOR
img[200:300,0:300] = 255,0,0

cv2.imshow('PRIMARY COLORS',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
