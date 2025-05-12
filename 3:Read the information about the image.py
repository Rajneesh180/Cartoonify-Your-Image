#3.Read the Information about the image

import cv2
img = cv2.imread('rdj.webp')
print(img.shape)

#(311, 553, 3)
#311 is the height of image in pixels
#553 is the width of image in pixels
#3 is the depth/channel number(RGB)
