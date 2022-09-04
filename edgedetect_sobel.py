# EDGE detection has 3 main types:
# 1.SOBEL 2.LAPLACIAN 3. CANNY
# SOBEL Technique(Take only Sudoku image)
import cv2
img=cv2.imread('sudoku.png',0) #to convert into greyscale
sobel_x=cv2.Sobel(img,cv2.CV_8U,dx=1,dy=0,ksize=-1)
#CV_8U - unsigned 8 bit/pixel
#kernel - will define the size of convolution
sobel_y=cv2.Sobel(img,cv2.CV_8U,dx=0,dy=1,ksize=-1)
sobel_f=cv2.bitwise_or(sobel_x,sobel_y) #convolution happens
cv2.imshow('SOBEL X IMAGE',sobel_x)
cv2.imshow('SOBEL Y IMAGE',sobel_y)
cv2.imshow('SOBEL IMAGE',sobel_f)
cv2.waitKey(0)
cv2.destroyAllWindows()