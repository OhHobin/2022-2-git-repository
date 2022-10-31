import numpy as np 
import csv
from matplotlib import pyplot as plt 

x = []
f = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week06/input.csv', 'r', encoding='UTF-8')
f_data = csv.reader(f)

for i in f_data:
	try:
		i[:] = map(int, i[:])
		x.append(i)
	except:
		pass

data = np.array(x[1:])

plt.scatter(data[:, 0], data[:, 1]) 
plt.title("Gross National Income (KRW 10,000) / Year")
plt.xlabel("Year")
plt.ylabel("GNI(KRW 10,000)")
plt.axis([1985, 2030, 1000, 4000])
plt.show()

f.close()