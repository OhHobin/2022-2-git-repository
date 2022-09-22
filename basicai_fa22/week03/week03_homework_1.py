xfile = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week03/sales.txt', 'r', encoding='UTF-8')
yfile = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week03/summary.txt', 'w', encoding='UTF-8')
xlist = xfile.readlines()
total = 0
avg = 0
result = []
for i in range(len(xlist)):
    xlist[i] = xlist[i].rstrip('\n')
    total += int(xlist[i])
    avg = total/len(xlist)

result.append('총매출 = %d\n' %total)
result.append('평균 일매출 = %.1f' %avg)

for i in range(len(result)):
    yfile.write(result[i])

xfile.close()
yfile.close()