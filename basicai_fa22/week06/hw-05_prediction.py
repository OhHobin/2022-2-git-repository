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

# 학습율 (learning_rate)
learning_rate = 0.9

costs = []
# random 한 값으로 w, b를 초기화 합니다.
w = np.random.uniform(low=1, high=5)
b = np.random.uniform(low=0, high=5)
print('w: ', w, 'b: ', b)
c = 0
while True:
    c += 1
    y_hat = w * x + b

    error = ((y_hat - y)**2)
    cost = error.mean()

    if cost < 0.005:
        break

    w = w - learning_rate * ((y_hat - y) * x).mean()
    b = b - learning_rate * (y_hat - y).mean()

    costs.append(cost)

    if c % 5 == 0:
        print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(
            c, w, b, cost))

print("----" * 15)
print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(c, w, b, cost))


# 예측
w = 65.35381
b = -64.30628
x = 1990 # True : 24
y_predict = x / 1000 * w + b
print(x, ':', y_predict * 1000)

x = 2000 # True : 36
y_predict = x / 1000 * w + b
print(x, ':', y_predict * 1000)

x = 2010 # True : 47
y_predict = x / 1000 * w + b
print(x, ':', y_predict * 1000)

x = 2020 # True : ?
y_predict = x / 1000 * w + b
print(x, ':', y_predict * 1000)