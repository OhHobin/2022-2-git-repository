xfile = open('C:/Users/LG/매수종목2.txt', 'r', encoding='UTF-8')
a = xfile.readlines()

x = {}
for i in a:
    i = i.strip()
    k, v = i.split()
    x[k] = v

print(x)
xfile.close()