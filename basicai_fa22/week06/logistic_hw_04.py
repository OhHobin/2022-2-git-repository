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
x = data[:, 0] / 100
y = data[:, 1]


def sigmoid(x):  # 시그모이드 함수 정의
    return 1/(1+np.exp(-x))

w = np.random.uniform(low=0, high=20)
b = np.random.uniform(low=-20, high=10)
print('w: ', w, 'b: ', b)

num_epoch = 500000
learning_rate = 100
costs = []
eps = 1e-5

for epoch in range(num_epoch):
    hypothesis = sigmoid(w * x + b)

    cost = y * np.log(hypothesis + eps) + (1 - y) * np.log(1 - hypothesis + eps)
    cost = -1 * cost
    cost = np.mean(cost)

    if cost < 0.00005:
        break

    w = w - learning_rate * ((hypothesis - y) * x).mean()
    b = b - learning_rate * (hypothesis - y).mean()

    costs.append(cost)

    if epoch % 50 == 0:
        print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(
            epoch, w, b, cost))

print("----" * 15)
print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(epoch, w, b, cost))

plt.figure(figsize=(10, 7))
plt.plot(costs)
plt.xlabel('Epochs')
plt.ylabel('Costs')
plt.show()