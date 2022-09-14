x = input().split()
y = input().split()
for i in range(len(y)):
    y[i]  = int(y[i])
print({x[0]:y[0], x[1]:y[1]})
