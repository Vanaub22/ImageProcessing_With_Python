#shortcut method for converting into greyscale image
import cv2
img=cv2.imread('abc1.jpg',0)#0 here converts into greyscale
cv2.imshow('Greyscale Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()