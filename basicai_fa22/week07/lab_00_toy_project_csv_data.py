import csv
from symbol import yield_expr
import numpy as np

l = []
f = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week07/wine.csv', 'r', encoding='UTF-8')
f_data = csv.reader(f)

for i in f_data:
	l.append(i)
data = np.array(l)

x = data[1:, 1:]  # 와인 정보
y = data[1:, 0]   # 정답

print(x[3])
print(np.shape(y))