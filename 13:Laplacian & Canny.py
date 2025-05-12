#13. LAPLACIAN and CANNY

import cv2
img = cv2.imread('rdj.webp',0) #gray scale

laplacian = cv2.Laplacian(img,cv2.CV_8U)
cv2.imshow('LAPLACIAN IMAGE',laplacian)

canny = cv2.Canny(img,90,200) #90,200 is thresh and max value
cv2.imshow('CANNY IMAGE',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
