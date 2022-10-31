#############################################
# Image Save using Pillow
#############################################

import numpy as np
from PIL import Image

image = Image.open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week05/week05_lab/dip_for_numpy/images/img_041.png')
print(type(image)) # <class 'PIL.PngImagePlugin.PngImageFile'>
img_np = np.array(image)
print(img_np.shape, img_np.dtype, img_np.size, img_np.ndim)
i = Image.fromarray(img_np)
i.save('test.bmp', 'bmp')