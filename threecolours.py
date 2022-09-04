#to have all three primary colours in one image
import cv2
import numpy as np
img=np.zeros((300,300,3)) #creates a black background
#to slice and assign new colors
img[0:100,0:300]=0,255,0 #green colour
img[100:200,0:300]=0,0,255 #red colour
img[200:300,0:300]=255,0,0 #blue colour
cv2.imshow('Primary Colours',img)
cv2.waitKey(0)
cv2.destroyAllWindows()