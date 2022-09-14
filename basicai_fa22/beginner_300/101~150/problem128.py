x = input("주민등록번호: ")
y = x.split("-")[1]
if 0 <= int(y[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")