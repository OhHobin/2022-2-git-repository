x = ''
y = 0
for i in range(1, 101):
    x += str(i)
for i in range(len(x)):
    y += int(x[i])
print(y)