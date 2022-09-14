x = []
for i in range(1001):
    x.append(str(i))
a = 0
for i in range(len(x)):
    if x[i].find('1') == True:
        a += 1

print(a)