import random

x = int(input())
y = int(input())
a = []
for i in range(y):
    a.append(int(input(':')))
t, c = 0, 0
for i in range(len(a)):
    t += a[i]
    if t > x:
        break
    c += 1
        

print(c)