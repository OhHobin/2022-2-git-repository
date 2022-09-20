x = open('C:/Users/LG/2022-2-git-repository/basicai_fa22/week03/input.txt', 'r', encoding = 'UTF-8')
xtxt = x.readlines()
xlist = []
for i in range(len(xtxt)):
    xlist.append(xtxt[i].split())
    if xlist[i][-1] == '+':
        print(int(xlist[i][0]) + int(xlist[i][1]))    
    elif xlist[i][-1] == '-':
        print(int(xlist[i][0]) - int(xlist[i][1]))
    elif xlist[i][-1] == '*':
        print(int(xlist[i][0]) * int(xlist[i][1]))
    else:
        print(int(xlist[i][0]) / int(xlist[i][1]))