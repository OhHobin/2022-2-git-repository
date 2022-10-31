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
x = data[:, 0]
y = data[:, 1]
def sigmoid(x):  # 시그모이드 함수 정의
    return 1/(1+np.exp(-x))

w = np.random.uniform(low=0, high=20)
b = np.random.uniform(low=-20, high=10)
print('w: ', w, 'b: ', b)

num_epoch = 10000

learning_rate = 0.5

costs = []

eps = 1e-5

for epoch in range(num_epoch):
    hypothesis = sigmoid(w * x + b)

    cost = y * np.log(hypothesis + eps) + (1 - y) * np.log(1 - hypothesis + eps)
    cost = -1 * cost
    cost = cost.mean()

    if cost < 0.0005:
        break

    # reference : https://nlogn.in/logistic-regression-and-its-cost-function-detailed-introduction/
    w = w - learning_rate * ((hypothesis - y) * x).mean()
    b = b - learning_rate * (hypothesis - y).mean()

    costs.append(cost)

    if epoch % 5000 == 0:
        print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(
            epoch, w, b, cost))

print("----" * 15)
print("{0:2} w = {1:.5f}, b = {2:.5f} error = {3:.5f}".format(epoch, w, b, cost))

# 예측
w = 154.12681
b = -130.98310
x = 45 # True : 0
x = x / 100
pred_y = sigmoid(w * x + b)
print(pred_y)

x = 100 # True : 1
x = x / 100
pred_y = sigmoid(w * x + b)
print(pred_y)

x = data[:, 0] 
y = data[:, 1]

org_x = np.linspace(0, max(x), 100)
pred_y = sigmoid(w * (org_x / 100) + b)

plt.scatter(x, y) 
plt.title("V_EC vs BREAKDOWN")
plt.xlabel("V_EC")
plt.ylabel("BREAKDOWN Pass(1)/Fail(0)")
plt.plot(org_x, pred_y, 'r')
# plt.axis([0, 420, 0, 50])
plt.show()