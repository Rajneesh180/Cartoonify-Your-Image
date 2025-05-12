#11. HSV FILTER (HUE,SATURATION,VALUE/LUMINIOUSITY)

import numpy as np
import cv2

img = cv2.imread('abcd.webp') #will read the image
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV FILTER',img_hsv)

cv2.imshow('HUE FILTER',img_hsv[:,:,0]) #HUE
cv2.imshow('SATURATION FILTER',img_hsv[:,:,1]) #SATURATION FILTER
cv2.imshow('VALUE FILTER',img_hsv[:,:,2]) #VALUE FILTER

cv2.waitKey(0)
cv2.destroyAllWindows
