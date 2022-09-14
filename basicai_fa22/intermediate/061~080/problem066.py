def solution(t, l):
    answer = []
    for p in t:
        answer.append(c(p, l))
    return answer

def c(p, l):
    par = l.index(l[0])
    for t in p:
        if t in l:
            if par > l.index(t):
                return '불가능'
            par = l.index(t)
    return '가능'

t = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG', 'AEBFDGCH']
l = 'ABCD'

print(solution(t, l))