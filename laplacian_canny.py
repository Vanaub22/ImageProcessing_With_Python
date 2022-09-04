import cv2
img=cv2.imread('abc1.jpg',0) #greyscale image
laplacian=cv2.Laplacian(img,cv2.CV_8U)
cv2.imshow('Laplacian Image',laplacian)
canny=cv2.Canny(img,90,200) #tuning parameters: threshold and maximum value
cv2.imshow('Canny Image',canny)
#edge detetcion is better in Canny
cv2.waitKey(0)
cv2.destroyAllWindows()