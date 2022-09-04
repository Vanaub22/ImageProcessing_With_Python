#Face and Eye recognition
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
img=cv2.imread('abc.jpg')#reading the image
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=9)
eyes=eye_cascade.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=20)
#scaleFactor and minNeighbors are the the tuning parameters
#for faces minNeighbors --> 1-15
#for eyes minNeighbors --> 12-30
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    #h and w are height and width respectively
for x,y,w,h in eyes:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
cv2.imshow('Face and Eye Recognition',img)
cv2.waitKey(0)
cv2.destroyAllWindows()