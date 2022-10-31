import csv
import numpy as np

l = []
f = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week07/wine.csv', 'r', encoding='UTF-8')
f_data = csv.reader(f)

for i in f_data:
	l.append(i)
data = np.array(l)

x = data[1:, 1:]  # 와인 정보
y = data[1:, 0]   # 정답

# 2. 선택
# # 정규화 방법
# x_max = x.max(axis=0)
# x_normal = x / x_max

# 3. 원 핫 인코딩 (one-hot encoding)
label = []
# 0 : '1'
# 1 : '2'
# 2 : '3'

for name in y:
    if name == '1':
        label.append(0)
    elif name == '2':
        label.append(1)
    elif name == '3':
        label.append(2)

print(label)
print(x)

# one-hot encoding
num = np.unique(label, axis=0)          # 행 끼리 중복된 값 지우기
num = num.shape[0]                      
encoding = np.eye(num)[label]          # 정방단위행렬
print(encoding)
y_hot = encoding.copy()
# x : 입력 데이터, y : 출력(클래스) 데이터 - one-hot encoding
print(label[0], y_hot[0])
print(label[70], y_hot[70])
print(label[-1], y_hot[-1])