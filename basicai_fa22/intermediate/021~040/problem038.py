x = input().split()
y = []
for i in range(len(x)):
    c = 0
    for j in range(len(x)):
        if x[i] < x[j]:
            c += 1
    y.append(c)
r = 0
s = 0
y = sorted(y)
for i in range(0, len(y)-1):
    if s == 3:
        break
    else:
        if y[i] == y[i+1]:
            r += 1
        else:
            r += 1
            s += 1
print(r)