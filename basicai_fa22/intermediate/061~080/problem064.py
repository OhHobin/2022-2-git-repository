x = int(input())
result = 0
while True:
    if x % 7 ==0:
        result += x//7
        print(result)
        break
    x -= 3
    result += 1
    if x < 0:
        print(-1)
        break