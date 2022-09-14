x = input("우편번호: ")
x = x[:3]
if x in ["010", "011", "012"]:
    print("강북구")
elif x in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")