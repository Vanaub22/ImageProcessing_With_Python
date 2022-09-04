# Realtime object detection using a video
import cv2
cascade_src='cars.xml'
video_src='video1.avi'
cap=cv2.VideoCapture(video_src)
car_cascade=cv2.CascadeClassifier(cascade_src)
while True:
    ret,img=cap.read()#we are reading the data from the cap variable
    if(type(img)==type(None)):
        break
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#greyscale image
    cars=car_cascade.detectMultiScale(grey,1.1,1)
    for(x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        #cv2.rectangle(source, starting point, ending point, thickness)
    cv2.imshow('Video',img)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
