#############################################
# Image Concatnation
#############################################

import numpy as np
from PIL import Image

img = Image.open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week05/week05_lab/dip_for_numpy/images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

i = np.array(img)
i = i[np.newaxis, :, :, :]
print(i.shape)
print('---------')
i2 = np.concatenate((i, i), 0)
print(i2.shape)
print('---------')
n = np.repeat(i, 99).reshape(99, 680, 1024, 3)
i3 = np.concatenate((i, n), 0)
print(i3.shape)
print('---------')
m = np.repeat(i, 999).reshape(999, 680, 1024, 3)
i4 = np.concatenate((i, m), 0)
print(i4.shape)