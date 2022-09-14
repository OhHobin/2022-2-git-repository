def solution(point, dish):
    dish -=1
    answer = 0
    s = sorted(point)
    while True:
        p = point.pop(0)
        if s[0]==p:
            if dish == 0:
                break        
            dish-=1
            s.pop(0)
        else:
            point.append(p)
            dish = len(point)-1 if dish==0 else dish-1
        answer+=1
    return answer

def solution(접시점수, 먹을접시위치):
    먹을접시위치 -= 1
    정답 = 0
    정렬된접시점수 = sorted(접시점수)
    while True:
        맨앞접시 = 접시점수.pop(0)
        if 정렬된접시점수[0] == 맨앞접시:
            if 먹을접시위치 == 0:
                break
            먹을접시위치 -= 1
            정렬된접시점수.pop(0)
        else:
            접시점수.append(맨앞접시)
            먹을접시위치 = len(접시점수) - 1 if 먹을접시위치 == 0 else 먹을접시위치 - 1
        정답 += 1
    return 정답
x = input()
y = int(input())
print(solution(x, y))