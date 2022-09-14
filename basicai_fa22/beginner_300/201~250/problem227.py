def printmxn(x, y):
    for i in range(len(x)):
        if (i+1) % y == 0:
            print(x[i])
        else:
            print(x[i], end='')

printmxn("아이엠어보이유알어걸", 3)