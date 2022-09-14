people = 0
total = 0
n = 4
while(True):
    total = people*(people-1)/2
    if n < total:
        break
    people+=1
times = int(people-(total-n)-1)
print([times,people])