#solid colours - red, blue and green
#Red background
import numpy as np
import cv2
img=np.zeros((250,250,3))#black background
#img[:] --> to select the whole image
img[:]=0,0,255#assignment in (B,G,R) format
cv2.imshow('Red Background',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
