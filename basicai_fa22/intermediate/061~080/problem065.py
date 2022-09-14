x = [1,2,3,4]
y = ['a', 'b', 'c', 'd']
q = [0, 0, 0, 0]
for i in range(len(x)):
    q[i] = (x[i], y[i])

print(q)