nationWidth = {
'korea': 220877,
'Rusia': 17098242,
'China': 9596961,
'France': 543965,
'Japan': 377915,
'England' : 242900}

x = []
for i in nationWidth:
    x.append(nationWidth[i]) 
x = sorted(x)

for i in range(len(x)):
    if x[i] == nationWidth['korea']:
        o = i+1
        break
reverse_dict= dict(map(reversed,nationWidth.items()))
p = x[o]
q = reverse_dict[p]
w = nationWidth[q]
ww = nationWidth['korea'] - w
print(q, -ww)