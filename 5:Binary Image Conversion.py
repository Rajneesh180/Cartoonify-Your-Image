#5.BINARY IMAGE CONVERSION(High contrast)
import cv2
img = cv2.imread('abcd.webp',0)#0 is given to obtain grayscale image
cv2.imshow('ORIGINAL IMAGE',img)
cv2.imshow('GRAY SCALE IMAGE',img)#displays gray scale image
cv2.waitKey(2000)

#============cv2.threshold(src,thresh value,max val,type of conversion)
ret,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ret is a dummy variable , we do not use it anywhere
#only binARY variable is taken into consideration

cv2.imshow('BINARY IMAGE',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
