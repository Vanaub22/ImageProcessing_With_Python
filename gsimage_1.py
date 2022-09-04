#greyscale image(black and white)
import cv2
img=cv2.imread('abc1.jpg')
#convert to greyscale image
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('ORIGINAL',img)
cv2.imshow('GREYSCALE VERSION',grey)
cv2.waitKey(0)
cv2.destroyAllWindows()