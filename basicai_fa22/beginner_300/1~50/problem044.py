file_name = "보고서.xlsx"
for i in range(len(file_name)):
    if file_name[i] == '.':
        print(file_name[i+1], end='')
        print(file_name[i+2], end='')
        print(file_name[i+3], end='')
        print(file_name[i+4])