import cv2
from cv2 import destroyAllWindows
import numpy as np
#to create a black image and a window
windowName='Drawing'
cv2.namedWindow(windowName)
img=np.zeros((500,500,3))
#mouse callback function
#flags and params are not used at all, but it is compulsory in mouse callback fn.
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:#left button double click
        #arguments in order (source, coordinates, radius, colour, thickness)
        cv2.circle(img,(x,y),40,(0,255,0),-1)
    if event==cv2.EVENT_RBUTTONDBLCLK:#right button double click
        cv2.circle(img,(x,y),30,(255,255,255),-1)
    if event==cv2.EVENT_LBUTTONDOWN:#left button
        cv2.circle(img,(x,y),20,(0,255,255),-1)
    if event==cv2.EVENT_RBUTTONDOWN:#right click
        cv2.circle(img,(x,y),10,(0,0,255),-1)
cv2.setMouseCallback(windowName,draw_circle)#function call
while(True):
    cv2.imshow(windowName,img)
    if cv2.waitKey(1)==ord('q'):
        break
cv2,destroyAllWindows()

