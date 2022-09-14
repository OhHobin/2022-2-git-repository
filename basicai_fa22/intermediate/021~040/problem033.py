x = input().split()
for i in range(len(x)):
    x[i]  = int(x[i])
for i in range(len(x)-1, -1, -1):
    print(x[i], end = ' ')