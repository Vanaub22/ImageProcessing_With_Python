#accessing the webcam using python and opencv
import cv2
cap=cv2.VideoCapture(0)#0 takes the default camera of laptop
#otherwise put 1 for secondary webcam device
while True:
    ret,frame=cap.read()#it is reading the video from my port
#ret and frame are 2 variables to be taken, but only frame will be used
#ret is a dummy variable
    cv2.imshow('My Live Sketch',frame)
    if cv2.waitKey(1)==13:#13 is the ASCII vlue of the Enter key
        break
cap.release()#it releases the port number
#if cap.release is not performed, the webcam drivers may get corrupted
cv2.destroyAllWindows()