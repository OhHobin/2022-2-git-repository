x = input().split()
xs = set(x)
dd = {}
for key in xs:
    dd[key] = x.count(key)

print(f'{max(dd, key=dd.get)}(이)가 총 {max(dd.values())}표로 반장이 되었습니다.')