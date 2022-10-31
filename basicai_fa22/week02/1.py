import numpy as np
x = [['0', '1', '2'], ['3', '4', '5']]
print(x)
for i in x:
    i[:] = map(int, i[:])
x = np.array(x)

print(x)
print(np.min(x, 1))
print(np.sum(x, 1))