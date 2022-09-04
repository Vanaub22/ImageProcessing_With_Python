import cv2
import numpy as np
img=np.zeros((500,500,3))#black background
#cv2.rectangle(source, starting point, ending point, thickness)
cv2.rectangle(img,(200,200),(450,450),(0,255,0),2)
#use negative thickness to have a filled solid figure
cv2.imshow('Rectangle',img)#green rectangles
cv2.waitKey(0)
cv2.destroyAllWindows()