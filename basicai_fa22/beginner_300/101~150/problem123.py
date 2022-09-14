x = {"달러": 1167, 
     "엔": 1.096, 
     "유로": 1268, 
     "위안": 171}
y = input("입력: ")
num, currency = y.split()
print(float(num) * x[currency], "원")