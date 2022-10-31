import numpy as np
from matplotlib import pyplot as plt
import csv

# BREAKDOWN
# 0 : BREAKDOWN Pass, 1 : BREAKDOWN Fail
l = []
f = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week06/logistic_input.csv', 'r', encoding='UTF-8')
d = csv.reader(f)
for i in d:
    try:
        i[:] = map(int, i[:])
        l.append(i)
    except:
        pass
data = np.array(l[1:])

plt.scatter(data[:, 0], data[:, 1])
plt.title("V_EC vs BREAKDOWN")
plt.xlabel("V_EC")
plt.ylabel("BREAKDOWN Pass(1)/Fail(0)")
plt.grid()
plt.show()