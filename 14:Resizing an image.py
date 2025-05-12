#14. RESIZING AN IMAGE - SCALING AN IMAGE
import cv2
import numpy as np
img = cv2.imread('rdj.webp')
cv2.imshow('original image',img)
cv2.waitKey(2000)

#SCALE DOWN THE IMAGE
img_sc = cv2.resize(img,None,fx = 0.75 , fy = 0.75)
cv2.imshow('SCALE DOWN',img_sc)

#SCALE UP THE IMAGE
img_sc1 = cv2.resize(img,None,fx = 2,fy = 2)
cv2.imshow('SCALE UP',img_sc1)

#SCALING USING THE CUSTOM DIMENSION
img_sc2 = cv2.resize(img,(1000,400)) #1000 is length in pixel , 400 is width in pixel
cv2.imshow('SCALING - CUSTOM DIMENSIONS',img_sc2)

cv2.waitKey(0)
cv2.destroyAllWindows()
