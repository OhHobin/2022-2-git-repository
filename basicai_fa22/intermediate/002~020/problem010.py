x = int(input())
for i in range(x-1, -1, -1):
    print(' '* i, end=' ')
    print('*'*(2*(5 - i)-1))
