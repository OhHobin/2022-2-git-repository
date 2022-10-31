#############################################
# NCHW? NHWC?
#############################################

import numpy as np
from PIL import Image

img = Image.open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week05/week05_lab/dip_for_numpy/images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

np_img = np.array(img)
np_img = np_img[np.newaxis, :, :, :]
print(np_img.shape)     
print('------------')
np_img = np.transpose(np_img, (0, 3, 1, 2))        #NCHW 변경
print(np_img.shape)
print('------------')
np_img = np.transpose(np_img, (0, 2, 3, 1))        #다시 NHWC 변경
print(np_img.shape)

# 4차원에서 절대적인 값 
# N(ndim)
# C(color)
# H(height)
# W(width)