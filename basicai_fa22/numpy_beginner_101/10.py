import numpy as np

a = np.array([1, 2, 3])
b =  np.concatenate((np.repeat(a[0], 3), np.repeat(a[1], 3), np.repeat(a[2], 3), a, a, a))
print(b)