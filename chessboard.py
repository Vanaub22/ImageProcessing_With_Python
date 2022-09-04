# MINOR PROJECT: to create an 8x8 chessboard without using loops
# program developed by Anuvab Chakravarty
import numpy as np
import cv2
img=np.zeros((400,400,3))#200x200 pixels in black
# 1st 2 rows
img[0:50,0:50]=255,255,255
img[50:100,50:100]=255,255,255
img[0:50,100:150]=255,255,255
img[50:100,150:200]=255,255,255
img[0:50,200:250]=255,255,255
img[50:100,250:300]=255,255,255
img[0:50,300:350]=255,255,255
img[50:100,350:400]=255,255,255
#2nd 2 rows
img[100:150,0:50]=255,255,255
img[150:200,50:100]=255,255,255
img[100:150,100:150]=255,255,255
img[150:200,150:200]=255,255,255
img[100:150,200:250]=255,255,255
img[150:200,250:300]=255,255,255
img[100:150,300:350]=255,255,255
img[150:200,350:400]=255,255,255
#3rd 2 rows
img[200:250,0:50]=255,255,255
img[250:300,50:100]=255,255,255
img[200:250,100:150]=255,255,255
img[250:300,150:200]=255,255,255
img[200:250,200:250]=255,255,255
img[250:300,250:300]=255,255,255
img[200:250,300:350]=255,255,255
img[250:300,350:400]=255,255,255
#last 2 rows
img[300:350,0:50]=255,255,255
img[350:400,50:100]=255,255,255
img[300:350,100:150]=255,255,255
img[350:400,150:200]=255,255,255
img[300:350,200:250]=255,255,255
img[350:400,250:300]=255,255,255
img[300:350,300:350]=255,255,255
img[350:400,350:400]=255,255,255
cv2.imshow('Chessboard',img)
cv2.waitKey(0)
cv2.destroyAllWindows()