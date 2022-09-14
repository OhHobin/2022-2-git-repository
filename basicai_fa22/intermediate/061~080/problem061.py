x = input()
y = sorted(list(set(x)))
r = ''
for s in y:
    r += s
    r += str(x.count(s))
print(r)