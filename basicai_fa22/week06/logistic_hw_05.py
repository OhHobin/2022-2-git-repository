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

# 예측
w = 154.12681
b = -130.98310
x = 45 # True : 0
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 60 # True : 0
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 52 # True : 0
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)


x = 57 # True : 0
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 98 # True : 1
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 108 # True : 1
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)

x = 91 # True : 1
x = x / 100
pred_y = sigmoid(w * x + b)
print('x = ', x*100, 'pred: ', pred_y)