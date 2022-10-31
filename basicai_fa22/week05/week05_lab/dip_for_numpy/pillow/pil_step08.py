#############################################
# Image Concatnation
#############################################

import numpy as np
from PIL import Image

img = Image.open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week05/week05_lab/dip_for_numpy/images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>
np_img = np.array(img)
np_img_1 = 255 - np_img
img2 = Image.fromarray(np_img_1)
img2.show()

np_img_2 = 255 - np_img[:,:,0]
print(np_img.shape)
np_img[:, :, 0] = np_img_2
print(np_img.shape)
img3 = Image.fromarray(np_img)
img3.show()