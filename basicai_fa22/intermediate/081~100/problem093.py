def sol(x, y):
    r = 0
    temp = []

    if x == 0:
        r = len(y) * 6
        return r

    for i in y:
        if i in temp:
            r += 1
        else:
            if len(temp) < x:
                temp.append(i)
            else:
                temp = temp[1:] + [i]
            r += 6
    return r

x = int(input())
y = input().split()

print(sol(x, y))