import numpy as np 
from matplotlib import pyplot as plt 
import csv

def error(y_hat, yd):
	b = (y_hat - yd) ** 2
	return b

x = []
f = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week06/input.csv', 'r', encoding='UTF-8')
f_data = csv.reader(f)
for i in f_data:
	try:
		i[:] = map(int, i[:])
		x.append(i)
	except:
		pass
data = np.array(x[1:])

xd = data[:, 0]
yd = data[:, 1]

w = np.random.uniform(low=1, high=10)
b = np.random.uniform(low=0, high=10)
print('w: ', w, 'b: ', b)
y_hat = w * xd + b          
e = error(y_hat, yd)     # cost
print('error: ', e)
print('shape: ', e.shape)

cost = e.mean()           # 1/m
print('cost: ', cost)