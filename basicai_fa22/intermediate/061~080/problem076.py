import numpy as np

t = 5
p = 3

x = [[1, 0, 0, 1, 0],
          [0, 1, 0, 0, 1],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0]]

s = 0
for i in range(t - p + 1):
    for j in range(p):
        if np.sum(x[i:p+i, j:p+j]) > s: 
            s = np.sum(x[i:p+i, j:p+j])
print(s)