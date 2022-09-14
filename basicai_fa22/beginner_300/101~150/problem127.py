x = input("주민등록번호: ")
x = x.split("-")[1]
if x[0] == "1" or x[0] == "3":
    print("남자")
else:
    print("여자")