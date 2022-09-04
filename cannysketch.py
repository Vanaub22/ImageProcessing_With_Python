#canny sketch(edge detection)
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    canny=cv2.Canny(frame,20,150)
    cv2.imshow('My Canny Sketch',canny)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()