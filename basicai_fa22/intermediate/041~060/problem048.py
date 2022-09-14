from dataclasses import replace


x = input()
x = x.replace('A', 'a')
x = x.replace('B', 'b')
x = x.replace('c', 'C')
x = x.replace('d', 'D')
print(x)