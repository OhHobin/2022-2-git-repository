from ast import operator


x = input().split()
y = input().split()
d = dict()
ny = []

for i in range(len(y)):
    c = 4
    for j in range(len(y)):
        if int(y[i]) > int(y[j]):
            c -= 1
    ny.append(c)

d = {x[0]:ny[0], x[1]:ny[1], x[2]:ny[2], x[3]:ny[3]}
nd = dict(sorted(d.items(), key=lambda x:x[1]))
print(nd)