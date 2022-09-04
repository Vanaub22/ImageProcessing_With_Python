#hsv filter(hue, saturation,value/luminousity)
import numpy as np
import cv2
img=cv2.imread('abc1.jpg')#will read the image
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Filter', img_hsv)
cv2.imshow('Hue Filter',img_hsv[:,:,0])#hue filter
cv2.imshow('Saturation Filter',img_hsv[:,:,1])#saturation filter
cv2.imshow('Value Filter',img_hsv[:,:,2])#value filter
cv2.waitKey(0)
cv2.destroyAllWindows()