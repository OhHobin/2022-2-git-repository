import datetime

x = datetime.datetime.now()
for day in range(5, 0, -1):
    y = datetime.timedelta(days = day)
    r = x - y
    print(r)