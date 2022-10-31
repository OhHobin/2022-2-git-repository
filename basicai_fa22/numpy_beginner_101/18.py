import numpy as np

arr = np.arange(9).reshape(3,3)
arr = arr[(2, 1, 0), :]
print(arr)