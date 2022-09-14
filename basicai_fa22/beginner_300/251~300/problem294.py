xfile = open('C:/Users/LG/매수종목1.txt', 'r', encoding='UTF-8')
x = []
x = xfile.readlines()
for i in range(len(x)):
    x[i] = x[i].rstrip('\n')
print(x)
xfile.close()