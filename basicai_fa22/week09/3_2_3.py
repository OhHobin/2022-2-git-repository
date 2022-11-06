import numpy as np
from matplotlib import pyplot as plt

def step_fucntion(x):
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_fucntion(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()