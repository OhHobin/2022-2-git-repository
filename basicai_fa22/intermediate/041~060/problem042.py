import datetime

x = int(input())
y = int(input())

def findDay(a, b):
    d = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    print(d[datetime.date(2020, a, b).weekday()])

findDay(x, y)