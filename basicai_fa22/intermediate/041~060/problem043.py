x = int(input())
y = []

while x:
    y.append(x % 2)
    x = x//2

for i in range(len(y)-1, -1, -1):
    print(y[i], end='')