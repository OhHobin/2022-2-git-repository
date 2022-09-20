x = input('입력: ')
x = x.replace('.', '')
x = x.replace(' ', '')

for i in range(len(x)):
    if i == len(x) - 1:
        print('true')
    elif x[i] == x[-(i+1)]:
       continue
    else:
        print('false')
        break