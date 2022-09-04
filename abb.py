import os
 
# importing io from skimage
import skimage
from skimage import io
 
# way to load car image from file
file = os.path.join(skimage.data_dir,'abc.jpg')
 
 
cars = io.imread(file)
 
# way to show the input image
io.imshow(cars)
io.show()
