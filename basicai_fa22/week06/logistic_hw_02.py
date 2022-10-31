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
import math

# array (numpy)
def sigmoid(x):  # 시그모이드 함수 정의
    return 1/(1+np.exp(-x))

# x is scalar 1 EA
# def sigmoid(x):  # 시그모이드 함수 정의
#     return 1/(1+math.exp(-x))
x = np.arange(-10.0, 10.0, 0.1)
print(x.shape, x.ndim, x.size)
print(type(x))
# print(x)
y = sigmoid(x)
# plt.scatter(data[:, 0], data[:, 1])
plt.plot(x, y, 'g')
plt.plot([0, 0], [1.0, 0.0], ':')  # 가운데 점선 추가
plt.title('Sigmoid Function')
plt.show()


# W 값에 따른 경사도 변화
x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(0.5*x)
y2 = sigmoid(x)
y3 = sigmoid(2*x)

plt.plot(x, y1, 'r', linestyle='--')  # W의 값이 0.5일때
plt.plot(x, y2, 'g')  # W의 값이 1일때
plt.plot(x, y3, 'b', linestyle='--')  # W의 값이 2일때
plt.plot([0, 0], [1.0, 0.0], ':')  # 가운데 점선 추가
plt.title('Sigmoid Function')
plt.show()

# b 값에 따른 좌, 우 이동
x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x+0.5)
y2 = sigmoid(x+1)
y3 = sigmoid(x+1.5)

plt.plot(x, y1, 'r', linestyle='--')  # x + 0.5
plt.plot(x, y2, 'g')  # x + 1
plt.plot(x, y3, 'b', linestyle='--')  # x + 1.5
plt.plot([0, 0], [1.0, 0.0], ':')  # 가운데 점선 추가
plt.title('Sigmoid Function')
plt.show()