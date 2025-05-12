#2.CREATE A DUPLICATE IMAGE WITH ANY OTHER EXTENSION
import cv2 # impoting the library
img = cv2.imread('rdj.webp')#reading the image
cv2.imshow('OUTPUT1',img)#displaying the image
cv2.imwrite('ameen.png',img)#creates a new/duplicate image

cv2.waitKey(3000)
cv2.destroyAllWindows()
