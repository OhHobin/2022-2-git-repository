def print_score(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    print(total/len(x))
    
print_score ([1, 2, 3])