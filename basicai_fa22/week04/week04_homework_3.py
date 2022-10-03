import csv
import numpy as np

inp = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week04/input.csv', 'r', encoding='UTF-8')
read = csv.reader(inp)
x = []
avg = []
total = []

for i in read:
    try:
        x.append(i)
        i[1:] = map(int, i[1:])
        total.append(np.sum(i[1:]))
        avg.append(np.mean(i[1:]))
    except:
        pass

for i in range(len(x)):
    if i == 0:
        x[i].append('합계')
        x[i].append('평균')
    else:
        x[i].append(total[i-1])
        x[i].append(avg[i-1])

outp = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week04/output.csv', 'w', newline='', encoding='UTF-8')
write = csv.writer(outp)
for i in range(len(x)):
    if i == len(x)-1:
        write.writerow(x[i])
    else:
        write.writerow(x[i])

inp.close()
outp.close()