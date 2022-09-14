per = ["10.31", "", "8.00"]
x = []
for i in per:
    try:
        x.append(float(i))
    except:
        x.append(0)

print(x)