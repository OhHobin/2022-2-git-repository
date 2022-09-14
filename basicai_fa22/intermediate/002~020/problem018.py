x = input().split()
t = 0
for i in range(len(x)):
    t += int(x[i])
print(int(t/len(x)))