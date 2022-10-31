#############################################
# Convert Color image to Gray image using PILLOW
#############################################

import numpy as np
from PIL import Image

img = Image.open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week05/week05_lab/dip_for_numpy/images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>
g_img = np.array(img.convert('L'))
i = Image.fromarray(g_img)
i.show()