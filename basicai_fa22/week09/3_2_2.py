import numpy as np

def step_fucntion(x):
    y = x > 0 
    return y.astype(np.int)

x = np.array([-1.0, 1.0, 2.0])
y = x > 0 
print(y)
y = y.astype(np.int)
print(y)