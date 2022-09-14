data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
x = []
for i in range(len(data)):
    for j in range(len(data[i])):
        x.append(data[i][j] + data[i][j] * 0.00014)
print(x)