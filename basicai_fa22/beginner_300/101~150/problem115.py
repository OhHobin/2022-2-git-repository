x = int(input("입력값: "))
y = x - 20
if y > 255:
    print(255)
elif y < 0:
    print(0)
else:
    print(y)