x = input("주민등록번호: ")
q = int(x[0]) * 2 + int(x[1]) * 3 + int(x[2]) * 4 + int(x[3]) * 5 + int(x[4]) * 6 + \
        int(x[5]) * 7 + int(x[7]) * 8 + int(x[8]) * 9 + int(x[9]) * 2 + int(x[10])* 3 + \
        int(x[11])* 4 + int(x[12]) * 5
w = 11 - (q % 11)
e = str(w)

if x[-1] == e[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")