#10.CHECKER BOARD or CHESS BOARD
import numpy as np
import cv2

img = np.zeros((300,300,3)) #200*200 pixels black image created
img[0:100,0:100] = 255,255,255
img[100:200,100:200] = 255,255,255

img[0:100,200:300]=255,255,255
img[200:300,0:100]=255,255,255
img[200:300,200:300]=255,255,255

cv2.imshow('CHESS BOARD',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
