import numpy as np
from PIL import Image


i_c = np.zeros((600, 800, 3), dtype = np.uint8)  
i_c[:, :, 0] = 255   # uint 이므로 0 ~ 255
                     # red를 나타내는 컬러 0 을 가장 밝게 255로

i_c2 = np.zeros((600, 800, 3), dtype = np.uint8)  
i_c2[:, :, 0] = 255
i_c2[:, :, 1] = 255
i_c2[:, :, 2] = 255

i_c3 = np.zeros((600, 800, 4), dtype = np.uint8)  
i_c3[:, :, 0] = 255
i_c3[:, :, 1] = 255
i_c3[:, :, 2] = 255

xxx = Image.fromarray(i_c)
yyy = Image.fromarray(i_c2)
zzz = Image.fromarray(i_c3, mode = 'CMYK')#
##xxx.show()
#yyy.show()
#zzz.show()
print(i_c.shape)