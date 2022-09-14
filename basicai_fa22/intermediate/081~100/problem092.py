import csv

f = open('C:/Users/LG/Documents/1.csv', 'r', encoding='utf-8')
r = csv.reader(f)
for i in r:
    s1, s2 = '', ''
    for j in i[1].replace(',', ''):
        if j == '3':
            s1 += '1'
            s2 += '2'
        elif j == '4':
            s1 += '2'
            s2 += '2'
        elif j == '6':
            s1 += '1'
            s2 += '5'
        else:
            s1 += j
            s2 += '0'
    print(int(s1), int(s2))