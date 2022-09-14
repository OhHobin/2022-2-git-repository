import random as r

l = [chr(i) for i in range(65, 91)]
total_medicine = []
medicine = []

for i in range(100):
    total_medicine.append(r.sample(l, 8))

x = input().split()
xl = []
for i in total_medicine:
    if len(set(i) & set(x[0])) == int(x[1]):
        xl.append(i)

print(len(xl))