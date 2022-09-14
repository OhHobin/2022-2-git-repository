def solution(n):
    x='1'
    if n == 1:
        return x
    for i in range(1,n):
        x = rule(x)
    return x

def rule(n):
    num_l = max([int(i) for i in n])
    d = [str(i)+str(str(n).count(str(i))) for i in range(1,num_l+1)]
    return ''.join(d)