per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print('예외 발생 O')
    else:
        print('예외 발생 X')
    finally:
        print('변환')