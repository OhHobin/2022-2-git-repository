import random  as r

class_score = []
total_score = []
avg = []
first = 0
total_avg = 0

for i in range(7):
    class_score = []
    for i in range(30):
        x = []
        for i in range(5):
            x.append(r.randint(0, 101))
        class_score.append(x)
    total_score.append(class_score)

for c in total_score:
    for s in c:
        total_avg += sum(s)/5
    avg.append(total_avg // 30)
    total_avg = 0

print(avg)
print(int(sum(avg)/len(avg)))