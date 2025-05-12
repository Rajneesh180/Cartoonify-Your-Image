#6.SOLID BACKGROUNDS - BLACK or WHITE
#create a white background using openCV and numpy

import numpy as np
import cv2

img = np.ones((500,500,3))#500 is length in pixels,500 is breadth in pixels,3 is the channel number

cv2.imshow('White background',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Make it as np.zeros for black color
