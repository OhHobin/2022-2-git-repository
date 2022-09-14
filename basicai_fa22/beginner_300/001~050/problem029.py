string = 'abcdfe2a354a32a'
string = list(string)
for i in range(len(string)):
    if string[i] == 'a':
        string[i] = 'A'
for i in range(len(string)):
    print(string[i], end = '')