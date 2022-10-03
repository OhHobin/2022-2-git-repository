x = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week04/list.txt', 'r', encoding='UTF-8')
xlist = x.readlines()
for i in range(len(xlist)):
    xlist[i] = int(xlist[i].rstrip())
print('min:', min(xlist), 'max:', max(xlist))