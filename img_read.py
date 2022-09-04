#to read an image
import cv2 #importing of cv2/opencv lib
img=cv2.imread('abc1.jpg')
cv2.imshow('IMAGE',img)#display
cv2.waitKey(3000)#waiting time in milliseconds
#on putting 0, image will not disappear
cv2.destroyAllWindows()