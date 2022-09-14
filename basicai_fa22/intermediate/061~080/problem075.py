x = input()
y = [3, 6, 9, 33, 36, 39, 63, 66, 69, 93]
a = 0
for i in range(int(x)+1):
    a += y.count(i)

print(a)