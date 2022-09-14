x = input().split()
for i in range(len(x)):
    x[i]  = int(x[i])
if x == x.sort():
    print('YES')
else:
    print('NO')