x = input().split()
for i in range(len(x)):
    x[i]  = int(x[i])
print(x[0]//x[1], x[0]%x[1])