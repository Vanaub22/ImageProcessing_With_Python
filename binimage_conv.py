#binary image conversion(high contrast)
import cv2
img=cv2.imread('abc1.jpg',0)#0 is given to obtain greyscale image
cv2.imshow('Greyscale Image',img)#displays the image
cv2.waitKey(3000)
#cv2.threshold(src, thresh value, maximum value, type of conversion)
ret,binary=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('Binary Image',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()