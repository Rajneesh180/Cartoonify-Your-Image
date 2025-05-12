#16.CIRCLE

import cv2
import numpy as np

img = np.zeros((500,500,3)) #black image background
#cv2.circle(src,st point , radius , color , thickness)
cv2.circle(img,(250,250),100,(0,0,255),-2)

cv2.imshow('CIRCLE',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
