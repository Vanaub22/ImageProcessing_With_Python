#to create a duplicate image with any other extension
import cv2
img=cv2.imread('abc1.jpg')#reading the image
cv2.imshow('OUTPUT',img)
cv2.imwrite('abc1_duplicate.png',img)#creates duplicate image
cv2.waitKey(3000)
cv2.destroyAllWindows()