x = input("입력: ")
xlist = x.split( )

if xlist[2] == '+':
    print(int(xlist[0])+int(xlist[1]))
elif xlist[2] == '-':
    print(int(xlist[0])-int(xlist[1]))
elif xlist[2] == '*':
    print(int(xlist[0])*int(xlist[1]))
else:
    print(int(xlist[0])/int(xlist[1]))