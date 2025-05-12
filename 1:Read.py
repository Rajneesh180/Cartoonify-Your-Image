#1.READ AN IMAGE

import cv2 #importing of cv2/opencv lib to our program
img = cv2.imread('rdj.webp')#reading the image
cv2.imshow('IMAGE',img)#display the image

cv2.waitKey(0)#3000 is milliseconds, give 0 if you want image for ever
cv2.destroyAllWindows()
