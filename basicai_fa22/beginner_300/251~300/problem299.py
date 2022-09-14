data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except:
        print('인덱스 오버')