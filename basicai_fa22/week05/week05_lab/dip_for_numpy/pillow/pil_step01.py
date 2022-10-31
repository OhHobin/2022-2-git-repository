#############################################
# Image Read & Show
#############################################

import numpy as np
from PIL import Image

image = Image.open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week05/week05_lab/dip_for_numpy/images/baby.png')
image.show()
print(type(image))