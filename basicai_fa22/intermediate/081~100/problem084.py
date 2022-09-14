x = input(':')
xl = []
for i in range(len(x)):
    for j in range(len(x)):
        if i != j:    
            xl.append(x[i]+x[j])

print(max(xl))