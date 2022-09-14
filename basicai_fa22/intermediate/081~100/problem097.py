def sol(n,l):
    answer = 0
    man = [0]*n
    while sum(l)!=0:
        for j in range(len(man)):
            if man[j] == 0 and l:
                man[j]+=l.pop(0)
        man = list(map(lambda x : x-1,man))
        answer+=1
    answer+=max(man)
    return answer

n = 3
l = [0, 0, 0]

print(sol(n, l))