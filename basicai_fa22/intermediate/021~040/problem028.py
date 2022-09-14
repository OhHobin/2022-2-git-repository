x = input()
for i in range(len(x)):
    try:
        print(x[i]+x[i+1])
    except:
        pass