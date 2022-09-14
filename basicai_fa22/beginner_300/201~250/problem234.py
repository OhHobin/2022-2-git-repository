def pickup_even(x):
    y = []
    for i in range(len(x)):
        if x[i] % 2 == 0:
            y.append(x[i])
    print(y)

pickup_even([3, 4, 5, 6, 7, 8])