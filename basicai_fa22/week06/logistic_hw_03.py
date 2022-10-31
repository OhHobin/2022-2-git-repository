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

w = np.random.uniform(low=0, high=1)
b = np.random.uniform(low=0, high=1)
print('w: ', w, 'b: ', b)

hypothesis = sigmoid(w * x + b)

# 방법 1 -> 최적화 어려움, local minimum에 빠질 우려가 있음
error = (hypothesis - y) ** 2
cost = error.mean()
print('cost: ', cost)  # 이와 같은 cost는 최적화가 어려움

# 방법 2
cost = y * np.log(hypothesis) + (1 - y) * np.log(1 - hypothesis)
cost = -cost.mean()
print('cost: ', cost)