x = input().split()
for i in range(len(x)):
    x[i] = int(x[i])

x.sort(reverse=True)
print(x[0])