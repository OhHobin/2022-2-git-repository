x = 4
if x <= 1:
    print('소수 O')
elif x == 2:
    print('소수 X')
else:
    for i in range(2, x):
        if x % i == 0:
            print('소수 X')
            break
    else:
        print('소수 O')