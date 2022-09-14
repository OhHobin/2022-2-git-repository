flag = [] 
for i in range(5):
    flag.append(input('깃발 값과 함께 입력하세요 :').split(' '))

for i in range(5):
    for j in range(5):
        if flag[i][j] == '1':
            flag[i][j] = 'f'
            try:
                flag[i][j+1] = '*'
                flag[i][j-1] = '*'
                flag[i+1][j] = '*'
                flag[i-1][j] = '*'
            except:
                pass
        else:
            continue
for i in range(5):
    for j in range(5):
        print(flag[i][j], end=' ')
    print('')