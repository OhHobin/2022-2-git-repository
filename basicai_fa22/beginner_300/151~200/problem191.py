data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j] + data[i][j] * 0.00014)