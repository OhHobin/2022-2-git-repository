def math(e):
    c = 0
    cc = 0
    ccc = 0
    cccc = 0
    for i in range(len(e)):
        if e[i] == '(':
            c += 1
        elif e[i] == ')':
            cc += 1
        elif e[i] == '{':
            ccc += 1
        elif e[i] == '}':
            cccc += 1
    if c != cc or ccc != cccc:
        return False
    else:
        return True

while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) :')
    if order == '1':
        ex = input('데이터를 입력하세요 :')
        print(math(ex))
    else:
        break