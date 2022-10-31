#############################################
# Dimension Expansion using numpy
#############################################

import numpy as np
from PIL import Image

img = Image.open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week05/week05_lab/dip_for_numpy/images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>
i = np.array(img)
print(i.shape)
print(np.ndim(i))
print('-----------')
i2 = np.reshape(i, (1, 680, 1024, 3))
print(i2.shape)
print(np.ndim(i2))
print('-----------')
i3 = np.reshape(i2, (680, 1024, 3))
print(i3.shape)
print(np.ndim(i3))
print('-----------')
i4 = np.reshape(i3, (2, -1))
print(i4.shape)
print(np.ndim(i4))