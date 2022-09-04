#Resizing or scaling an image
import cv2
import numpy as np
img=cv2.imread('abc1.jpg')
cv2.imshow('Original Image',img)
cv2.waitKey(2000)
#Scaling down the Image
img_scd=cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow('Scaled down to 75%',img_scd)
#Scaling up the Image
img_scu=cv2.resize(img,None,fx=1.25,fy=1.25)
cv2.imshow('Scaled up to 200%',img_scu)
#Scaling using custom dimensions
img_cust=cv2.resize(img,(1000,400)) #(length,breadth) in pixel
cv2.imshow('Scaling - Custom dimensions',img_cust)
cv2.waitKey(0)
cv2.destroyAllWindows()