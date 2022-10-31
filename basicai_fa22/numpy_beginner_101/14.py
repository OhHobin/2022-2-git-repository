import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

b = np.array(a[(5 <= a)&(a <= 10)])
print(b)