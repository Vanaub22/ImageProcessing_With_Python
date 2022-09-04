#creating a white background using openCV and numpy
from cv2 import destroyAllWindows
import numpy as np
import cv2
#np.zeros for black
img=np.ones((500,500,3))#length,breadth,channel number
cv2.imshow('White Background',img)
cv2.waitKey(0)
cv2.destroyAllWindows()