#9.RGB EXTRACTION
#RED TINTED IMAGE

import numpy as np
import cv2
img = cv2.imread('su.png')
cv2.imshow('ORIGINAL IMAGE',img)

B,G,R = cv2.split(img)
zeros = np.zeros(img.shape[:2],dtype = 'uint8')
#uint8 - sets the values in the range of 0 to 255

cv2.imshow('RED TINTED IMAGE',cv2.merge([zeros,zeros,R]))

cv2.waitKey(0)
cv2.destroyAllWindows()
