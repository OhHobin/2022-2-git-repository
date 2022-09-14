url = "http://sharebook.kr"
for i in range(len(url)):
    if url[i] == '.':
        print(url[i+1], end='')
        print(url[i+2])