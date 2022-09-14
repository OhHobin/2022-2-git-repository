x = input()
c = 0
c_c = 0
for i in range(len(x)):
    if x[i] == '(':
        c += 1
    elif x[i] == ')':
        c_c += 1
if c == c_c:
    print('YES')
else:
    print('NO')