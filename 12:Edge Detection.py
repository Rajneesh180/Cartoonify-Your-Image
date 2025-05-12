#EDGE DETECTION - 3 MAIN TYPE
#1.SOBEL
#2.LAPLACIAN
#3.CANNY

#SOBEL TECHNIQUE :
#tAKE ONLY SUDOKU IMAGES

import cv2
img = cv2.imread('su.png',0) #to create into grayscale
sobel_x = cv2.Sobel(img,cv2.CV_8U,dx = 1 , dy = 0 , ksize = -1)
#CV_8U - unsigned 8 bit/pixel
#kernal - will define the size of convolution

sobel_y = cv2.Sobel(img,cv2.CV_8U,dx=0,dy=1,ksize=-1)
sobel_f = cv2.bitwise_or(sobel_x,sobel_y) #convolution

cv2.imshow('SOBEL X IMAGE',sobel_x)
cv2.imshow('SOBEL Y IMAGE',sobel_y)
cv2.imshow('SOBEL IMAGE', sobel_f)

cv2.waitKey(0)
cv2.destroyAllWindows()
