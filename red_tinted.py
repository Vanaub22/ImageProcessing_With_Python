#to create a red tinted image
import numpy as np
import cv2
img=cv2.imread('abc1.jpg')
cv2.imshow('Original Image',img)
B,G,R=cv2.split(img)
zeros=np.zeros(img.shape[:2],dtype='uint8')
#uint8 - sets the values in the range of 0 to 255
cv2.imshow('Red Tinted Image',cv2.merge([zeros,zeros,R]))
#use G and B in the correct positions for Green and Blue respectively
cv2.waitKey(0)
cv2.destroyAllWindows()