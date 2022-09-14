x = input().split()
for i in range(len(x)):
    x[i] = int(x[i])
for i in range(1, len(x)):
    if x[i-1] == x[i] - 1:
        if i == len(x) - 1:
            print('YES')
    else:
        print('NO')
        break