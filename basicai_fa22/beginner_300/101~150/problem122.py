x = int(input("score: "))
if 81 <= x <= 100:
    print("grade is A")
elif 61 <= x <= 80:
    print("grade is B")
elif 41 <= x <= 60:
    print("grade is C")
elif 21 <= x <= 40:
    print("grade is D")
else:
    print("grade is E")