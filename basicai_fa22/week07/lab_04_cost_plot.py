import csv
import numpy as np
from matplotlib import pyplot as plt

l = []
f = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week07/wine.csv', 'r', encoding='UTF-8')
f_data = csv.reader(f)

for i in f_data:
	l.append(i)
data = np.array(l)

x = np.array(data[1:, 1:], dtype=np.float16)  # 와인 정보
y = np.array(data[1:, 0], dtype=np.float16)   # 정답
# 2. 선택
# # 정규화 방법
x_max = x.max(axis=0)
x_normal = x / x_max

# 3. 원 핫 인코딩 (one-hot encoding)
label = []
# 0 : '1'
# 1 : '2'
# 2 : '3'

for name in y:
    if name == 1:
        label.append(0)
    elif name == 2:
        label.append(1)
    elif name == 3:
        label.append(2)

# one-hot encoding
num = np.unique(label, axis=0)          # 행 끼리 중복된 값 지우기
num = num.shape[0]                      
encoding = np.eye(num)[label]          # 정방단위행렬
y_hot = encoding.copy()

# 와인 데이터 : 13개
# 클래스 개수 : 3개

dim = 13
nb_classes = 3
print('x shape: ', x.shape, 'y shape: ', y.shape)
#x shape:  (178, 13) y shape:  (178,)

w = np.random.normal(size=[dim, nb_classes]) 
b = np.random.normal(size=[nb_classes])
#w shape:  (13, 3) b shape:  (3,)

print('w shape: ', w.shape, 'b shape: ', b.shape)

def cross_entropy_error(predict, target):
    delta = 1e-7
    return -np.mean(target * np.log(predict + delta))

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T

    x = x - np.max(x) # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))

hypothesis = softmax(np.dot(x_normal, w) + b)
print('hypothesis: ', hypothesis.shape)

# hypothesis:  (178, 3)

eps = 1e-7
cost = y_hot * np.log(hypothesis + eps)
cost = -cost.mean()
print('cost: ', cost)

num_epoch = 20000
learning_rate = 100
costs = []

m, n = x.shape

for epoch in range(num_epoch):
    z = np.dot(x_normal, w) + b
    hypothesis = softmax(z)

    cost = y_hot * np.log(hypothesis + eps)
    cost = -cost.mean()

    if cost < 0.00005:
        break
    w_grad = (1/m)*np.dot(x_normal.T, (hypothesis - y_hot))
    b_grad = (1/m)*np.sum(hypothesis - y_hot)

    w = w - learning_rate * w_grad
    b = b - learning_rate * b_grad

    costs.append(cost)

    if epoch % 50 == 0:
        print("{0:2} error = {1:.5f}".format(epoch, cost))

print("----" * 15)
print("{0:2} error = {1:.5f}".format(epoch, cost))
print("----" * 15)
#print(w, b)
plt.figure(figsize=(10, 7))
plt.plot(costs)
plt.xlabel('Epochs')
plt.ylabel('Costs')
plt.show()