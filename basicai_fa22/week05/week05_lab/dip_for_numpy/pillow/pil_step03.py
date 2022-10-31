#############################################
# Color Image Split & Merge using PILLOW
#############################################

import numpy as np
from PIL import Image

img = Image.open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week05/week05_lab/dip_for_numpy/images/img_041.png')
print(type(img)) # <class 'PIL.PngImagePlugin.PngImageFile'>

print(img.mode)
print(img.size)

i = np.array(img)

print(i.shape)

#bands = i.getbands()
r = i[:, :, 0]            #3차원의 3번째 color 중 0 이므로 red
g = i[:, :, 1]            #3차원의 3번째 color 중 1 이므로 greed  
b = i[:, :, 2]            #3차원의 3번째 color 중 2 이므로 blue
print(r.shape)

i_c = np.zeros(i.shape, dtype = np.uint8)   #변수 데이터 타입맞추기
                                            #defalut 값이 float
i_c[:, :, 0] = r
i_c[:, :, 1] = g
i_c[:, :, 2] = b

xxx = Image.fromarray(i_c)
xxx.show()