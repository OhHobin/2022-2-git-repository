import numpy as np

def pair_max(x, y):
    h = np.concatenate((x, y)).reshape(2, -1)
    c = np.max(h, 0)
    return c

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
c = pair_max(a, b)
print(c)