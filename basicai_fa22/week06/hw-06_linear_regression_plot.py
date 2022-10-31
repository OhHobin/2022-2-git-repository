import numpy as np
from matplotlib import pyplot as plt
import csv

xl = []
f = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week06/input.csv', 'r', encoding='UTF-8')
f_data = csv.reader(f)
for i in f_data:
	try:
		i[:] = map(int, i[:])
		xl.append(i)
	except:
		pass
data = np.array(xl[1:])

x = data[:, 0] / 2000
y = data[:, 1] / 2000
learning_rate = 0.5
c = 0
w = np.random.uniform(low=1, high=5)
b = np.random.uniform(low=0, high=5)
while True:
    c += 1
    y_hat = w * x + b

    error = ((y_hat - y)**2)
    cost = error.mean()

    if cost < 0.005:
        break

    w = w - learning_rate * ((y_hat - y) * x).mean()
    b = b - learning_rate * (y_hat - y).mean()

#w = 65.35381
#b = -64.30628
org_x = np.linspace(1985, 2025, 2000)
pred_x = org_x / 2000 
pred_y = w * pred_x + b
pred_y = pred_y * 2000 

plt.scatter(x*2000, y*2000) 
plt.title("Gross National Income (KRW 10,000) / Year")
plt.xlabel("Year")
plt.ylabel("GNI(KRW 10,000)")
plt.plot(org_x, pred_y)
plt.axis([1985, 2025, 1100, 3900])
plt.show()