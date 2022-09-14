x = input()
a = []
for i in range(50):
    a.append('=')

for i in range(len(x)):
    a[23 + i] = x[i]  

for i in range(len(a)):
    print(a[i], end = '')