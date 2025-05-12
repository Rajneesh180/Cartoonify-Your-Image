#21.FACE  & EYES RECOGNITION

import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('abc.jpg') #reading the image

#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img,scaleFactor = 1.1,minNeighbors =9)
eyes = eyes_cascade.detectMultiScale(img,scaleFactor = 1.1,minNeighbours = 18)
#scaleFactor and minNeighbors are the tuning parameters

for x,y,w,h in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
     cv2.imshow('FACE RECOGNITION',img)
    #w and h are height and width

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)
    cv2.imshow('FACE RECOGNITION',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
    
