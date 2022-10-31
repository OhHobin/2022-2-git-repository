from matplotlib import pyplot as plt
import csv
import numpy as np

l, d1, d2, d3 = [], [], [], []
f = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week07/wine.csv', 'r', encoding='UTF-8')
f_data = csv.reader(f)

for i in f_data:
	try:
		i[1:] = map(float, i[1:])
		i[-1] = i[-1]/10
	except:
		pass
	if i[0] == '1':
		d1.append(i[1:])
	elif i[0] == '2':
		d2.append(i[1:])
	elif i[0] == '3':
		d3.append(i[1:])
	else: 
		l.append(i)
bw = 0.25
d1 = np.array(d1)
d2 = np.array(d2)
d3 = np.array(d3)
x = np.arange(13)
l = sum(l, [])
l = l[1:]
md1 = np.mean(d1, axis = 0)
md2 = np.mean(d2, axis = 0)
md3 = np.mean(d3, axis = 0)
plt.bar(x, md1, bw, color = 'red')
plt.bar(x + bw, md2, bw, color = 'green')
plt.bar(x + 2*bw, md3, bw, color = 'blue')
plt.xticks(x, l, rotation=45, size = 5)
plt.title('red: 1, green: 2, blue: 3 [proline / 10]')
plt.show()