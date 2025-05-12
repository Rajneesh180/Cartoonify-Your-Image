#4.GRAYSCALE IMAGE (BLACK AND WHITE)

import cv2
img = cv2.imread('rdj.webp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert into grayscale
cv2.imshow('NORMAL IMAGE',img)#displays original image
cv2.imshow('GRAY SCALE IMAGE',gray)#displays grayscale image
cv2.imwrite('GrayScale.jpg',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

#SHORTCUT FOR GRAYSCALE IMAGE

import cv2
img = cv2.imread('rdj.webp',0)#0 here converts into grayscale
cv2.imshow('GRAY SCALE IMAGE',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
