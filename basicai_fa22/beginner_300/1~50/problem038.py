상장주식수 = "5,969,782,550"
상장주식수 = list(상장주식수)
for i in range(len(상장주식수)):
    if 상장주식수[i] == ',':
        상장주식수[i] = ''
for i in range(len(상장주식수)):
    print(상장주식수[i], end='')