x = [[0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0]]

def sol(x):
    w = len(x[0])
    h = len(x)
    xsum = [[0] * w for i in range(len(x))]
    for i in range(0, h):
        for j in range(0, w):
            if x[i][j] == 0:
                xsum[i][j] = 1
            else:
                xsum[i][j] = 0
    
    for i in range(1, h):
        for j in range(1, w):
            if xsum[i][j] == 1:
                xsum[i][j] = min(xsum[i-1][j-1], min(xsum[i-1][j], xsum[i][j-1])) + 1

    maxValue = 0
    x = 0
    y = 0
    for i in range(0, h):
        for j in range(0, w):
            if maxValue < xsum[i][j]:
                maxValue = xsum[i][j]
                x = i
                y = j

    print(maxValue, x, y)
    print(maxValue, 'X', maxValue)
    
    for i in range(x - (maxValue - 1), x + 1):
        for j in range(y - (maxValue - 1), y + 1):
            x[i][j] = '#'
    return x
    
sol(x)